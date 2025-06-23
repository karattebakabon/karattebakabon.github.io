#!/usr/local/bin/perl

#��������������������������������������������������������������������
#�� DayCounter : daycount.cgi - 2011/07/25
#�� Copyright (c) KentWeb
#�� http://www.kent-web.com/
#��������������������������������������������������������������������

# ���W���[���錾
use strict;

# �ݒ�t�@�C���捞
require './init.cgi';
my %cf = &init;

# �f�[�^��
my $q = $ENV{QUERY_STRING};
$q =~ s/\W//g;
$q ||= 'gif';

# ���X�V�����̏ꍇ
if ($q eq "yes" || ($cf{type} == 1 && $q eq "today")) {

	# �f�[�^�ǂݍ���
	my $count = &read_data;

	# �摜�\��
	&load_image($count);

# �X�V�����̏ꍇ
} else {

	# �f�[�^�X�V
	my $count = &renew_data;

	# �摜�\��
	&load_image($count);
}

#-----------------------------------------------------------
#  �f�[�^�X�V
#-----------------------------------------------------------
sub renew_data {
	# �{���̓����擾
	$ENV{TZ} = "JST-9";
	my ($mday) = (localtime(time))[3];

	# �݌v�t�@�C���ǂݍ���
	my $tdflg;
	open(DAT,"+< $cf{logfile}") or &error;
	eval "flock(DAT, 2);";
	my $data = <DAT>;

	# �݌v�t�@�C������
	my ($key, $count, $ip) = split(/\t/, $data);

	# IP�`�F�b�N
	my ($ipflg, $addr);
	if ($cf{ip_check}) {
		$addr = $ENV{REMOTE_ADDR};
		if ($addr eq $ip) { $ipflg++; }
	}

	# �{���̃J�E���g�����L�[�ɂ��ăJ�E���g�A�b�v
	if (!$ipflg) {
		# ����
		if ($key eq $mday) {
			$tdflg = 1;

		# ����
		} else {
			$tdflg = 2;
		}

		# �J�E���g�A�b�v
		$count++;

		# �݌v�t�@�C���X�V
		seek(DAT, 0, 0);
		print DAT "$mday\t$count\t$addr";
		truncate(DAT, tell(DAT));
	}
	close(DAT);

	# �{���X�V
	if ($tdflg == 1) {
		open(TOD,"+< $cf{today_dat}") or &error;
		eval "flock(TOD, 2);";
		my $log = <TOD>;
		seek(TOD, 0, 0);
		print TOD ++$log;
		truncate(TOD, tell(TOD));
		close(TOD);

	# ���ւ��̂Ƃ��i�{��/����X�V�j
	} elsif ($tdflg == 2) {
		open(TOD,"+< $cf{today_dat}") or &error;
		eval "flock(TOD, 2);";
		my $log = <TOD>;
		seek(TOD, 0, 0);
		print TOD "1";
		truncate(TOD, tell(TOD));
		close(TOD);

		open(YES,"+> $cf{yes_dat}") or &error;
		eval "flock(YES, 2);";
		print YES $log;
		close(YES);
	}

	return $count;
}

#-----------------------------------------------------------
#  �f�[�^���X�V
#-----------------------------------------------------------
sub read_data {
	# �����҂�����i�X�V�n�ƏՓˉ���j
	select(undef, undef, undef, 0.5);

	# �Ώۃf�[�^
	my %log = ( today => $cf{today_dat}, yes => $cf{yes_dat} );

	# �L�^�t�@�C���ǂݍ���
	open(DAT,"$log{$q}") or &error;
	my $count = <DAT>;
	close(DAT);

	return $count;
}

#-----------------------------------------------------------
#  �J�E���^�摜�o��
#-----------------------------------------------------------
sub load_image {
	my ($data) = @_;

	my ($digit,$dir);
	if ($q eq 'gif') {
		$digit = $cf{digit1};
		$dir = $cf{gifdir1};
	} else {
		$digit = $cf{digit2};
		$dir = $cf{gifdir2};
	}

	# ��������
	while ( length($data) < $digit ) {
		$data = '0' . $data;
	}

	# Image::Magick�̂Ƃ�
	if ($cf{image_pm} == 1) {
		require $cf{magick_pl};
		&magick($data, $dir);
	}

	# �摜���
	my @image;
	foreach ( split(//, $data) ) {
		push(@image,"$dir/$_.gif");
	}

	# �摜�A��
	require $cf{gifcat_pl};
	print "Content-type: image/gif\n\n";
	binmode(STDOUT);
	print &gifcat::gifcat(@image);
	exit;
}

#-----------------------------------------------------------
#  �G���[����
#-----------------------------------------------------------
sub error {
	# �G���[�摜
	my @err = qw{
		47 49 46 38 39 61 2d 00 0f 00 80 00 00 00 00 00 ff ff ff 2c
		00 00 00 00 2d 00 0f 00 00 02 49 8c 8f a9 cb ed 0f a3 9c 34
		81 7b 03 ce 7a 23 7c 6c 00 c4 19 5c 76 8e dd ca 96 8c 9b b6
		63 89 aa ee 22 ca 3a 3d db 6a 03 f3 74 40 ac 55 ee 11 dc f9
		42 bd 22 f0 a7 34 2d 63 4e 9c 87 c7 93 fe b2 95 ae f7 0b 0e
		8b c7 de 02	00 3b
	};

	print "Content-type: image/gif\n\n";
	foreach (@err) {
		print pack('C*', hex($_));
	}
	exit;
}

