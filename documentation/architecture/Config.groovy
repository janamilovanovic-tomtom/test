/*
 * Copyright (C) 2019 TomTom NV. All rights reserved.
 *
 * This software is the proprietary copyright of TomTom NV and its subsidiaries and may be
 * used for internal evaluation purposes or commercial use strictly subject to separate
 * license agreement between you and TomTom NV. If you are the licensee, you are only permitted
 * to use this software in accordance with the terms of your license agreement. If you are
 * not the licensee, you are not authorized to use this software in any manner and should
 * immediately return or destroy it.
 */

outputPath = 'build'

inputPath = '.'

inputFiles = [[file: 'instruction_engine_architecture.adoc', formats: ['html','pdf','docbook']]]

confluence = [:]
confluence.with {
    input = [[ file: "build/html5/instruction_engine_architecture.html",
               ancestorId: "736341954",
               preambleTitle: "Guidance Engine Architecture" ]]
    api = 'https://confluence.tomtomgroup.com/rest/api/'
    spaceKey = 'PU Navigation'
    createSubpages = true
    pagePrefix = '[NIE] '
    pageSuffix = ''
    credentials = "${System.getenv('CONFLUENCE_USER')}:${System.getenv('CONFLUENCE_PASSWORD')}".bytes.encodeBase64().toString()
    extraPageContent = '<ac:structured-macro ac:name="warning"><ac:parameter ac:name="title" /><ac:rich-text-body>This is a generated page, do not edit!</ac:rich-text-body></ac:structured-macro>'
}
