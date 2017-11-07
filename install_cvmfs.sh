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

