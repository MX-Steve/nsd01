#!/bin/bash
#系统安全设置

##########################################################
while true
do
clear
 echo "----------------------menu----------------------"
 echo "(1) 关闭selinux"
 echo "(2) 同步时间"
 echo "(3) ssh服务配置"
 echo "(0) exit"
 echo "-------------------------------------------------"
 echo -n "enter you chose[0-3]:"
 read num
 if [ ${num} -lt 0 -o ${num} -gt 3 ]
     then
       echo "this is not between 0-3"
 else
    if [ "${num}" == "1" ]
       then
       setenforce 0
       sed -i 's/SELINUX=.*/SELINUX=disabled/' /etc/selinux/config
 else
    if [ "${num}" == "2" ]
       then
       sed -i 's/ZONE=.*/ZONE="Asia\/Shanghai"/' /etc/sysconfig/clock
       echo `ntpdate -u ntp.api.bz&`
 else
    if [ "${num}" == "3" ]
##########################################################
       then
        while [ "1" == "1" ]
           do
           #clear
           echo "----------------------ssh.service----------------"
           echo "(1) 备份配置文件"
           echo "(2) 更改端口"
           echo "(3) 禁止密码为空用户登录"
           echo "(4) 登录限时(限定输入密码所需时间)"
           echo "(5) 限制3次登录密码错误，锁定该账户5分钟"
           echo "(6) 还原配置文件(必须先备份)"
           echo "(7) 重启sshd"
           echo "(8) 退回上一级"
           echo "-------------------------------------------------"
           read -p "enter you chose[0-7]:"

           if [ "${REPLY}" == "1" ]
              then
              cp /etc/ssh/sshd_config /etc/ssh/sshd_config_backup
              cp /etc/pam.d/sshd /etc/pam.d/sshd_backup
#########################################################################               
               echo "正在备份..."
               printf "\n"
               sleep 1
               i=0
               bar=''
               lable=('|' '\\' '-' '/')
               while [ $i -le 100 ]
               do
               #echo $i
               printf "[%-100s][%d%%][%c]\r" "$bar" "$i" "${lable[$i%4]}"
               bar='#'$bar
               let i++
               sleep 0.01
               done
               printf "\n"
###########################################################################
           elif [ "${REPLY}" == "2" ]
              then
              echo -n "set port:"
              read port
              sed -i 's/^#Port.*/Port '$port'/' /etc/ssh/sshd_config
              echo -e "OK"
           elif [ "${REPLY}" == "3" ]
              then
              sed -i 's/^#PermitEmptyPasswords.*/PermitEmptyPasswords no/' /etc/ssh/sshd_config

           elif [ "${REPLY}" == "4" ]
              then
              echo -n "set time(s):"
              read min
               if [ $min -le 10 ]
                 then
                 echo "the number is too small"
               else
                 sed -i 's/^#LoginGraceTime.*/LoginGraceTime '$min'm/' /etc/ssh/sshd_config
                 echo "[OK]"
               fi

           elif [ "${REPLY}" == "5" ]
              then
              sed -i '/#%PAM-1.0/a\auth       required     pam_tally2.so deny=3  lock_time=300 even_deny_root root_unlock_time=300' /etc/pam.d/sshd
              cat /etc/pam.d/sshd
              echo -e "\033[31m 注意:检查每列对齐,pam_tally2.so后为一个空格 \033[0m"
           elif [ "${REPLY}" == "6" ]
              then
              cp /etc/ssh/sshd_config_backup /etc/ssh/sshd_config
              cp /etc/pam.d/sshd_backup  /etc/pam.d/sshd
#########################################################################               
               echo "正在还原..."
               printf "\n"
               sleep 1
               i=0
               bar=''
               lable=('|' '\\' '-' '/')
               while [ $i -le 100 ]
               do
               #echo $i
               printf "[%-100s][%d%%][%c]\r" "$bar" "$i" "${lable[$i%4]}"
               bar='#'$bar
               let i++
               sleep 0.01
               done
               printf "\n"
###########################################################################
           elif [ "${REPLY}" == "7" ]
              then
              echo `service sshd stop` 
              echo `service sshd start`
           else
              break
           fi

           done
##########################################################
else
   exit
fi
 fi
  fi
   fi
echo -n "Do you contine [y/n]:"
 read contine
 if [ "${contine}" == "n" -o "${contine}" == "N" ]
    then
    exit
 fi
 done


