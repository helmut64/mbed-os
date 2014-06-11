"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from exporters import Exporter
from os.path import splitext, basename


class CodeRed(Exporter):
    NAME = 'CodeRed'
    TOOLCHAIN = 'GCC_CR'

    TARGETS = [
        'LPC1768',
        'LPC4088',
        'LPC1114',
        'LPC11U35_401',
        'LPC11U35_501',
        'UBLOX_C027',
		'LPC1549',
    ]

    def generate(self):
        libraries = []
        for lib in self.resources.libraries:
            l, _ = splitext(basename(lib))
            libraries.append(l[3:])

        ctx = {
            'name': self.program_name,
            'include_paths': self.resources.inc_dirs,
            'linker_script': self.resources.linker_script,
            'object_files': self.resources.objects,
            'libraries': libraries,
            'symbols': self.toolchain.get_symbols()
        }
        self.gen_file('codered_%s_project.tmpl' % self.target.lower(), ctx, '.project')
        self.gen_file('codered_%s_cproject.tmpl' % self.target.lower(), ctx, '.cproject')
