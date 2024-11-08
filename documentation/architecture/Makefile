#!/usr/bin/make -f

# Copyright (C) 2019 TomTom NV. All rights reserved.
#
# This software is the proprietary copyright of TomTom NV and its subsidiaries and may be
# used for internal evaluation purposes or commercial use strictly subject to separate
# license agreement between you and TomTom NV. If you are the licensee, you are only permitted
# to use this software in accordance with the terms of your license agreement. If you are
# not the licensee, you are not authorized to use this software in any manner and should
# immediately return or destroy it.

pdf: instruction_engine_architecture.pdf junction_model.pdf lane_guidance.pdf
html: instruction_engine_architecture.html junction_model.html lane_guidance.html

IE_ARCH_FILES = instruction_engine_architecture.adoc src/01_introduction_and_goals.adoc src/02_architecture_constraints.adoc src/04_solution_strategy.adoc src/05_building_block_view.adoc src/07_deployment_view.adoc src/11_technical_risks.adoc src/12_glossary.adoc

instruction_engine_architecture.pdf : $(IE_ARCH_FILES)
	asciidoctor --backend pdf --require asciidoctor-pdf --require asciidoctor-diagram instruction_engine_architecture.adoc

instruction_engine_architecture.html : $(IE_ARCH_FILES)
	asciidoctor --backend html5 --require asciidoctor-diagram instruction_engine_architecture.adoc

JUNCTION_MODEL_FILES=src/junction_model/junction_model_architecture.adoc src/junction_model/01_introduction_and_goals.adoc src/junction_model/02_relation_to_map.adoc src/junction_model/03_public_api.adoc src/junction_model/04_implementation.adoc

junction_model.pdf : $(JUNCTION_MODEL_FILES)
	asciidoctor --backend pdf --require asciidoctor-pdf --require asciidoctor-diagram src/junction_model/junction_model_architecture.adoc

junction_model.html : $(JUNCTION_MODEL_FILES)
	asciidoctor --backend html5 --require asciidoctor-diagram src/junction_model/junction_model_architecture.adoc

LANE_GUIDANCE_FILES=src/lane_guidance/lane_guidance_architecture.adoc src/lane_guidance/01_about_this_document.adoc src/lane_guidance/02_ux_requirements.adoc src/lane_guidance/03_api_concepts.adoc src/lane_guidance/04_clients.adoc src/lane_guidance/05_map_concepts.adoc src/lane_guidance/06_overall_architecture.adoc src/lane_guidance/07_individual_components.adoc src/lane_guidance/08_map_updates.adoc

lane_guidance.pdf : $(LANE_GUIDANCE_FILES)
	asciidoctor --backend pdf --require asciidoctor-pdf --require asciidoctor-diagram src/lane_guidance/lane_guidance_architecture.adoc

lane_guidance.html : $(LANE_GUIDANCE_FILES)
	asciidoctor --backend html5 --require asciidoctor-diagram src/lane_guidance/lane_guidance_architecture.adoc
