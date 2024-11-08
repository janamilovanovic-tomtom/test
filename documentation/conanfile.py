# Copyright (C) 2019 TomTom NV. All rights reserved.
#
# This software is the proprietary copyright of TomTom NV and its subsidiaries and may be
# used for internal evaluation purposes or commercial use strictly subject to separate
# license agreement between you and TomTom NV. If you are the licensee, you are only permitted
# to use this software in accordance with the terms of your license agreement. If you are
# not the licensee, you are not authorized to use this software in any manner and should
# immediately return or destroy it.

from conans import ConanFile


class DocumentationConan(ConanFile):
    python_requires = "documentation-generators/3.5.2@tomtom/stable"
    python_requires_extend = "documentation-generators.DoxygenGenerator"

    project_name = "Navigation Guidance Engine"
    name = "navigation-instruction-engine-documentation"
    input_folders = [
        "../navigation-instruction-engine",
    ]
    expected_output_files = [
        "xml/classtomtom_1_1navkit2_1_1instruction__engine_1_1internal_1_1_instruction_engine_interface.xml",
    ]
    apply_settings_for_language = "c++"
    file_patterns = ["*.hpp"]
