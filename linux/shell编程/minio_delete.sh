#!/bin/bash

function getMinioVolume {
minio_sdc5=`ls /storagedisk/*minio* -d`
minio_path=${minio_sdc5}
}

function getMinioLimit {
if [ -f .minio_limit.txt ];then
minio_limit=`cat .minio_limit.txt`	
elif [ `kubectl get pvc -n component  | grep  minio | head -1 | wc -l` -eq 1 ];then
limit=`kubectl get pvc -n component  | grep  minio | head -1 | awk '{print$4}' | awk -F 'Gi' '{print$1}' | awk '{print 0.8*$1}'`
echo $limit > .minio_limit.txt
exit
fi
}

function getMaxBucket {
du -sh `ls` | grep -Ev '[0-9]K|[0-9]M|^0|infra-model-manager' > .minio_sum.txt
Decimal=`awk -F . '{print$2}' .minio_sum.txt |awk  '{print$1}' | sed -r 's/[A-Z]//g'`
sed -ri 's/\.[0-9]//g' .minio_sum.txt
sed -i "s/T/${Decimal}00G/g" .minio_sum.txt
max_size=1
while read line
do
size=`echo ${line} | awk -F "G" '{print$1}' | awk -F "." '{print$1}'`
bucket=`echo ${line} | awk '{print$2}'`
if [ ${size} -gt ${max_size} ];then

  max_size=${size}
  max_bucket=${bucket}
fi
done < .minio_sum.txt


}

function getMaxDepth {
du -sh ${max_bucket}/* > .child_dir
sed -i '/^0/d' .child_dir
Decimal=`awk -F . '{print$2}' .child_dir |awk  '{print$1}' | sed -r 's/[A-Z]//g'`
sed -ri "s/.[0-9]T/${Decimal}00G/" .child_dir
size1=1
while read line
do
size_tmp=`echo ${line} | awk -F ' ' '{print$1}'`
path=`echo ${line} | awk -F " " '{print$2}'`
if [ `echo $size_tmp | grep G  | wc -l ` -eq 1 ];then
  size_tmp=`echo ${size_tmp} | awk -F 'G' '{print$1}' | awk -F '.' '{print$1}'`
if [ $size_tmp -gt $size1 ];then
    size1=$size_tmp
    max_path=${path}
fi
fi
done < .child_dir
}


function deleteByDate {
disk_usage=$(a=0;for i in $(cut -d 'G' -f1 ${minio_path}/.minio_sum.txt); do let a+=$i; done; echo $a)
while [ ${disk_usage} -gt ${minio_limit} ]
do
if [ 1000 -gt ${disk_usage} ] && [ ${disk_usage} -ge 100 ];then
	delete_speed=1000
elif [ ${disk_usage} -ge 1000 ];then
	delete_speed=10000
elif [ ${disk_usage} -lt 100 ];then
	delete_speed=100
fi
old_file=$(ls -rt  |head -${delete_speed})
du -sh `ls /storagedisk/*minio*/* -d` | grep -Ev 'infra-model-manager' > ${minio_path}/.minio_sum1.txt
sed -ri '/^[0-9]+K/d' ${minio_path}/.minio_sum1.txt
sed -ri '/^0/d' ${minio_path}/.minio_sum1.txt
Decimal=`awk -F . '{print$2}' ${minio_path}/.minio_sum1.txt |awk  '{print$1}' | sed -r 's/[A-Z]//g'`
sed -ri 's/\.[0-9]//g' ${minio_path}/.minio_sum1.txt
sed -i "s/T/${Decimal}00G/g" ${minio_path}/.minio_sum1.txt
disk_usage=$(a=0;for i in $(cut -d 'G' -f1 ${minio_path}/.minio_sum1.txt); do let a+=$i; done; echo $a)
echo $disk_usage
if [ ${disk_usage} -lt ${minio_limit} ];then
echo "当前磁盘利用率为:${disk_usage},小于${minio_limit},退出"
exit
else
echo "当前磁盘利用率为:${disk_usage},大于${minio_limit},开始执行删除"
echo "greater than ${minio_limit}"
echo "Start Delete File"
echo  ${old_file}
rm -f ${old_file}
fi
done
}

function main {

getMinioVolume
getMinioLimit
echo $minio_limit
cd ${minio_path}
getMaxBucket
echo "最大的bucket是${max_bucket}，容量为${max_size}G"
getMaxDepth
if [ -z ${max_path} ];then
	echo "get max_path fail"
else
cd ${minio_path}/${max_path}
echo "目前清理的路径为:`pwd`"
deleteByDate
fi
}

main
