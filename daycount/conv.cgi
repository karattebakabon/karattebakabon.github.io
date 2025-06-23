#!/usr/local/bin/perl

#��������������������������������������������������������������������
#�� DayCounter : conv.cgi - 2011/10/07
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������������������������
# [ Ver.2 ���� Ver.3 �փ��O��ϊ����邽�߂̃v���O�����ł� ]
# [ ���O�ϊ���́A�K���폜���Ă��������B                  ]
#
# [ �g���� ]
#   1. �udata�f�B���N�g���v�̃p�[�~�b�V������777�ɐݒ�
#   2. Ver.2�Ŏg�p���Ă����udaycount.dat�v���udata�f�B���N�g���v�ɒu���B
#   3. �udata�f�B���N�g���v�̒��Ɂutoday.dat�v�uyes.dat�v��u���A���Ƀp�[�~�b�V������666�ɂ���B
#   4. �uconv.cgi�v�ɃA�N�Z�X���A�u�ϊ�����!�v�̕����񂪕\�����ꂽ�琬���B
#   5. �uconv.cgi�v���폜����B

# ���W���[���錾
use strict;
use CGI::Carp qw(fatalsToBrowser);

require "./init.cgi";
my %cf = &init;

# ���f�[�^
my $oldfile = "./data/daycount.dat";

open(IN,"$oldfile") || die;
my $data = <IN>;
close(IN);

my ($key, $yes, $tod, $count, $ip) = split(/<>/, $data);

open(DAT,"+> $cf{logfile}") || die;
print DAT "$key\t$count\t$ip";
close(DAT);

open(DAT,"+> $cf{today_dat}") || die;
print DAT $tod;
close(DAT);

open(DAT,"+> $cf{yes_dat}") || die;
print DAT $yes;
close(DAT);

chmod( 0666, $cf{logfile}, $cf{today_dat}, $cf{yes_dat} );

print <<EOM;
Content-type: text/html

<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=shift_jis">
<title>�ϊ��v���O����</title>
</head>
<body>
�ϊ�����!
</body>
</html>
EOM

