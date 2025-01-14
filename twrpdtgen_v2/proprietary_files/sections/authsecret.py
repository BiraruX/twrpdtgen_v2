# BACKUP REPLACE FILE

#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from twrpdtgen_v2.proprietary_files.section import Section, register_section

class AuthsecretSection(Section):
	name = "Authsecret"
	interfaces = [
		"android.hardware.authsecret",
	]

register_section(AuthsecretSection)
