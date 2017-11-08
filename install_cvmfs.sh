#!/bin/sh 

# get the repo/key
wget -O /etc/yum.repos.d/cernvm.repo http://cvmrepo.web.cern.ch/cvmrepo/yum/cernvm.repo
wget -O /etc/pki/rpm-gpg/RPM-GPG-KEY-CernVM http://cvmrepo.web.cern.ch/cvmrepo/yum/RPM-GPG-KEY-CernVM

yum -y install cvmfs cvmfs-config-default

cat << EOF > /etc/cvmfs/default.local 
CVMFS_REPOSITORIES=cms.cern.ch,grid.cern.ch
CVMFS_QUOTA_LIMIT=18000
CVMFS_CACHE_BASE=/var/lib/cvmfs
CVMFS_HTTP_PROXY="http://t2-squid-01.to.infn.it:3128|http://t2-squid-02.to.infn.it:3128"
EOF

# start the service
service autofs restart
cvmfs_config setup
cvmfs_config probe

# specific for cms
mkdir -p /etc/cvmfs/CMS_SITECONF/local/JobConfig/
cp /cvmfs/cms.cern.ch/SITECONF/T1_IT_CNAF/JobConfig/site-local-config.xml /etc/cvmfs/CMS_SITECONF/local/JobConfig/

echo "export CMS_LOCAL_SITE=T1_IT_CNAF" > /etc/cvmfs/config.d/cms.cern.ch.local

cp /etc/cvmfs/config.d/cms.cern.ch.local /etc/cvmfs/config.d/cms.cern.ch.conf

service autofs restart
cvmfs_config setup
cvmfs_config probe
