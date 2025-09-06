#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/xiaomi',
    'vendor/xiaomi/pearl'
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
   	'vendor/bin/hw/android.hardware.security.keymint@1.0-service.mitee': blob_fixup()
		.replace_needed('android.system.keystore2-V1-ndk_platform.so', 'android.system.keystore2-V1-ndk.so')
		.replace_needed('android.hardware.security.keymint-V1-ndk_platform.so','android.hardware.security.keymint-V4-ndk.so')
		.replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
		.replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndk.so')
		.add_needed('android.hardware.security.rkp-V3-ndk.so'),

	'vendor/lib64/libmt_mitee@1.3.so': blob_fixup()
    .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so','android.hardware.security.keymint-V4-ndk.so'),

	('vendor/bin/hw/android.hardware.gnss-service.mediatek',
	'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
    .replace_needed('android.hardware.gnss-V1-ndk_platform.so','android.hardware.gnss-V1-ndk.so'),

	'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
    .replace_needed('android.hardware.power-V2-ndk_platform.so','android.hardware.power-V2-ndk.so'),

    ('vendor/lib64/mt6895/libcam.hal3a.so',
     'vendor/lib64/mt6895/libcam.hal3a.ctrl.so',
     'vendor/lib64/mt6895/libmtkcam_request_requlator.so'): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    ('vendor/lib64/lib3a.ae.pipe.so',
     'vendor/lib64/mt6895/libaaa_toneutil.so',
     'vendor/lib64/mt6895/lib3a.flash.so',
     'vendor/lib64/mt6895/lib3a.sensors.color.so',
     'vendor/lib64/mt6895/lib3a.sensors.flicker.so'): blob_fixup()
        .add_needed('liblog.so'),

    'vendor/lib64/libalhLDC.so': blob_fixup()
        .add_needed('libnativewindow.so')
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

    'vendor/lib64/libalLDC.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

    ('vendor/lib64/libnvram.so',
     'vendor/lib64/libsysenv.so',
     'vendor/bin/ioprofiler'): blob_fixup()
        .add_needed('libbase_shim.so'),

     'vendor/lib64/libthha.so': blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),

     'vendor/lib64/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_unlock')
        .add_needed('libbase_shim.so'),

    'vendor/lib64/mt6895/libmnl.so': blob_fixup()
        .add_needed('libcutils.so'),

     'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .add_needed('libprocessgroup.so')
        .add_needed('libprocessgroup_shim.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),

    ('vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service',
     'vendor/lib64/mt6895/libmtkcam_stdutils.so',
     'vendor/lib64/hw/mt6895/android.hardware.camera.provider@2.6-impl-mediatek.so',
     'vendor/lib64/hw/mt6895/vendor.mediatek.hardware.pq@2.15-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so'),

    'vendor/bin/hw/mtkfusionrild': blob_fixup()
        .add_needed('libutils-v32.so'),

    ('vendor/lib64/hw/mt6895/vendor.mediatek.hardware.pq@2.15-impl.so',
     'vendor/lib64/mt6895/libaalservice.so',
     'vendor/bin/mnld'): blob_fixup()
        .replace_needed('libsensorndkbridge.so', 'android.hardware.sensors@1.0-convert-shared.so'),

    'vendor/etc/sensors/hals.conf': blob_fixup()
        .regex_replace('android.hardware.sensors@2.X-subhal-mediatek.so', 'android.hardware.sensors@2.0-subhal-impl-1.0.so')
        .regex_replace('sensors.touch.detect.so', 'sensors.dynamic_sensor_hal.so'),

    'vendor/lib64/hw/audio.primary.mediatek.so': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libalsautils.so', 'libalsautilsv2.so'),

    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),

    ('vendor/etc/libnfc-nxp.conf',
     'vendor/etc/libnfc-nxp-pnscr.conf'): blob_fixup()
        .regex_replace('(NXPLOG_.*_LOGLEVEL)=0x03', '\\1=0x02')
        .regex_replace('NFC_DEBUG_ENABLED=1', 'NFC_DEBUG_ENABLED=0'),

    'vendor/bin/mi_thermald': blob_fixup()
        .binary_regex_replace(b'%d/on', b'%d/..'),

    'vendor/etc/init/android.hardware.neuralnetworks-shim-service-mtk.rc': blob_fixup()
        .regex_replace('start', 'enable'),

}  # fmt: skip

module = ExtractUtilsModule(
    'pearl',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
