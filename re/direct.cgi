#!/usr/local/bin/perl

#==================================================================
#
# Copyright (C) 2002 Imu http://ra-map.hp.infoseek.co.jp/
# 
#==================================================================

# TOP�y�[�W
$TOP = "";

# ���t���b�V�����g��
$RFRESH = "1";

# ���t���b�V�����ԁi�b�j
$TIME = "5";
# ���t���b�V�����ԁi�O��������Ă����Ƃ��j
$E_TIME = "1";

# �摜
$COUNT ="count01.gif";
# �w�i�A�e�L�X�g�̐F��
$body =	"<BODY TEXT=#000000 LINK=FF0000 VINK= BGCOLOR=#FFFFFF>";
../cgi-bin/re/?http://www.yahoo.co.jp/
###### �ݒ�I #######

$QUERY_DATA = $ENV{'QUERY_STRING'};

if( $ENV{'SCRIPT_NAME'} =~ /direct\.cgi/ ) { 
	print "Content-type: text/html\n\n"; 
}
if ($QUERY_DATA ne '') {
	print "<HTML lang=\"ja\"><HEAD>";
	print "<META HTTP-EQUIV=\"Content-type\" CONTENT=\"text/html; charset=Shift_JIS\">\n";
	print "$body\n";
	if ($RFRESH eq '1') { print "<META HTTP-EQUIV=\"refresh\" CONTENT=\"$TIME;url=$QUERY_DATA\">"; }
	print "<a href=\"$QUERY_DATA\">$QUERY_DATA</a><br>";
	if ($RFRESH eq '1') { print "�֓]����($TIME\sec)<br><img src=$COUNT>"; }
	else { print "��L�T�C�g�ɃW�����v���܂��B�����N���N���b�N���Ă�������"; }
	print "<hr size=1><div align=right><a href=\"http://ra-map.hp.infoseek.co.jp/\" target=\"_top\">imu</a></div></HEAD></HTML>";
	exit;
}else{
# �O����direct.cgi�ɓ����Ă����ꍇ�̏���
	print "<HTML><HEAD>";
	print "<META HTTP-EQUIV=\"refresh\" CONTENT=\"$E_TIME;url=$TOP\">";
	print "<a href=\"$TOP\">$TOP</a>";
	print "</HEAD></HTML>";
	exit;
}
