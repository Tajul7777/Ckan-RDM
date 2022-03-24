#!/usr/bin/python
# -*- coding: utf-8 -*-
# Importing modules

import pandas as pd
import re
import os

# import spacy

import spacy
from spacy import displacy
from spacy.matcher import Matcher
import visualise_spacy_tree
from IPython.display import Image, display

# load the year

papers_list = []
Years = [
    '2022',
    '2021',
    '2020',
    '2019',
    '2018',
    '2017',
    '2016',
    '2015',
    '2014',
    '2013',
    '2012',
    '2011',
    '2010',
    '2009',
    '2008',
    '2007',
    '2006',
    '2005',
    '2004',
    '2003',
    '2002',
    '2001',
    '2000',
    '1999',
    '1998',
    '1997',
    '1996',
    '1995',
    '1994',
    '0',
    ]

for Year in Years:
    papers_tmp = pd.read_csv('processed.csv')
    papers_tmp.Year = papers_tmp.Year.astype(str)
    papers_list.append(papers_tmp)

df = pd.concat(papers_list).reset_index(drop=True)


# function to modification areas, authors, titles

def modify(text):

    # removing new line characters

    text = re.sub('\n ', '', str(text))

    # removing multiple spaces

    text = re.sub(' +', ' ', str(text))

    # remove front and back space

    text = str(text).lstrip()

    # removing apostrophes

    text = re.sub("'s", '', str(text))

    # removing hyphens

    text = re.sub('-', ' ', str(text))
    text = re.sub('\xe2\x80\x94 ', '', str(text))
    text = re.sub(';', '', str(text))

    # text = re.sub("*",'',str(text))
    # removing quotation marks

    text = re.sub('"', '', str(text))

    # removing any reference to outside text

    text = re.sub("[\(\[].*?[\)\]]", '', str(text))

    return text


# preprocessing areas

df['research_area_modify'] = df['Research Area'].apply(modify)

# preprocessing authors

df['authors_modify'] = df['Authors'].apply(modify)

# preprocessing titles

df['title_modify'] = df['Title'].apply(modify)


# function to preprocess areas

def clean(text):

    # removing paragraph numbers

    text = re.sub('[0-9]+.\t', '', str(text))

    # removing new line characters

    text = re.sub('\n ', '', str(text))
    text = re.sub('\n', ' ', str(text))

    # removing multiple spaces

    text = re.sub(' +', ' ', str(text))

    # remove front and back space

    text = str(text).lstrip()

    # removing apostrophes

    text = re.sub("'s", '', str(text))

    # removing hyphens

    text = re.sub('-', ' ', str(text))
    text = re.sub('\xe2\x80\x94 ', '', str(text))
    text = re.sub(';', '', str(text))

    # removing quotation marks

    text = re.sub('"', '', str(text))

    # removing salutations

    text = re.sub("Mr\.", 'Mr', str(text))
    text = re.sub("Mrs\.", 'Mrs', str(text))

    # removing none fields

    text = re.sub('nan', '', str(text))

    # removing any reference to outside text

    text = re.sub("[\(\[].*?[\)\]]", '', str(text))

    # spilt the text

    text = ' '.join(text.split('|'))

    # remove front and back space

    text = str(text).lstrip()

    # removing multiple spaces

    text = re.sub(' +', ' ', str(text))

    # make  lower

    text = text.lower()

    # make tags
    # if(re.search("web engineering", str(text))):
        # df['tags'] = 'Information'
        # print(text)

    return text


# preprocessing areas

df['research_area_clean'] = df['Research Area'].apply(clean)

# lis of all subjects tag

web_engineering = [  # complete
    'web migration',
    'independent software vendors',
    'reverse engineering',
    'crowdsourcing',
    'sme',
    'process model',
    'web composition',
    'web components',
    'world wide web',
    'web systems',
    'software migration',
    'agile development',
    'search engines',
    'human computer interaction',
    'html5',
    'web application development',
    'web design',
    'web development',
    'cscw',
    'groupware',
    'end user development',
    'rest',
    'distributed systems',
    'information model',
    'user interaction',
    'ambient calculus',
    'wam',
    'dgs',
    'service oriented',
    'loose coupling',
    'web architecture',
    'webe',
    'software development',
    'software test',
    'cloud storage',
    'cloud security',
    'agile',
    'python',
    'api',
    'distributed computing',
    ]

cloud_computing = [  # complete
    'event driven',
    'micro service',
    'Hybrid communication',
    'wireless sensor network',
    'iot',
    'internet of things',
    'mixed traffic',
    'fault injection',
    'it sicherheit',
    'bewertungsverfahren',
    'technologieevalierung',
    'distributed computing',
    'c v2x',
    ' its g5',
    'scalability',
    'slo',
    'gqm',
    'resource management',
    'transformation strategy',
    'geodateninfrastruktur',
    'gdi',
    'disruptive innovation',
    'otrs',
    'slate',
    'audio encoding',
    'video encoding',
    'media encoding',
    '3D Realtime Animation',
    '3D Image Processing',
    'OFDM ',
    'orthogonal frequency division multiplexing',
    'cloudscale',
    'cloud',
    'computing',
    'cloud storage',
    'cloud security',
    ]

information_retrieval = [  # complete
    'informationssuche',
    'knowledge acquisition',
    'situation model',
    'text comprehension',
    'metadata management',
    'object detection and classification',
    'speech recognition',
    'language modeling',
    'clinical texts',
    'audio classification',
    'multimedia information',
    'distributed infrastructure',
    'image recognition',
    'tracking methods',
    'fusion methods',
    'web application',
    'game mechanics',
    'video analysis',
    'audio analysis',
    'cloud services',
    'encoding',
    'graphical user interfaces',
    'videoanalyse',
    'performance measurement',
    'visualisation',
    'automatic speech recognition',
    'data fusion',
    'amopa',
    'xtrieval',
    'mpeg',
    'umts',
    'crosslanguage',
    'query expansion',
    'musikerkennung',
    'semantic web',
    'ontology engineering',
    'knowledge graph',
    'search engine',
    'encryption',
    'privacy',
    'security',
    ]

deep_learning = [  # complte
    'supervised learning',
    'performance evaluation',
    'ddos',
    'software defined networking',
    'adversarial training',
    'adversarial network attacks',
    'cnn',
    'semi supervised learning',
    'unsupervised learning',
    'convolutional neural network',
    'virtual reality',
    'artificial intelligence',
    'support vector machine',
    'svm',
    'image segmentation',
    'object detection',
    'classification',
    'botnet traffic detection',
    'zero day attack',
    'reinforcement learning',
    'qlearning',
    'free space detection',
    'fisheye camera',
    'gait analysis',
    'verhaltensanalyse',
    'neuronale',
    'omnidirectional Camera',
    'active assisted living',
    'anomaanomaly detection',
    'ctu',
    'deep transfer learning',
    'ANN',
    'feature extraction',
    'pose estimation',
    'mask rcnn',
    'data augmentation',
    'audio signal processing',
    'audio captioning',
    'semiconductor defects',
    'person tracking',
    'pattern and image recognition',
    ' icei',
    'plant classification',
    'bird identification',
    'acoustic source localization',
    'bird sound recognition',
    'visual distortion',
    'obstacle recognition',
    'automated annotation',
    'sensor data',
    'topologieoptimierung',
    'sentiment analysis',
    'clef',
    'icei',
    'vhs',
    'computer vision',
    ]

big_data = [  # complete
    'internet of things',
    'iot',
    'wireless sensor network',
    'processor design',
    'microcontrollers',
    'pattern recognition',
    'database management system',
    'artificial intelligence',
    'datenbank',
    'machine learning',
    'database',
    'instance search',
    'generic object detection',
    'intelligent video analysis',
    'cnn',
    'multimedia analysis',
    'duplicate detection',
    'data reduction',
    'rapid evaluation',
    'sift',
    'knn',
    'keyframe extraction',
    'adaboost',
    'fin whale detection',
    'blue whale detection',
    'large data',
    'intelligente systeme collaboration',
    'queriable networks',
    'algorithmen',
    'web',
    'kontexterkennung',
    'social media',
    'cisg',
    'data faults',
    'quality of data',
    'data and warranty',
    'business analytics and big data',
    'mass customization',
    'business intelligence',
    'typology',
    'business analytics',
    'data literacy',
    'datadriven',
    'design science research',
    'knowledge boundaries',
    'boundary objects',
    'electronic markets',
    'data science',
    'semantic text mining',
    'text mining',
    'semantic text',
    'leximancer',
    'content analysis',
    'pedagogy',
    'analysis',
    'datathons',
    'open data',
    'data scientist',
    'information systems',
    'interdisciplinarity',
    'data mining',
    'sap',
    'agile',
    'datenvolumen',
    'hadoop',
    'visual communication',
    'multimodality',
    'convergence',
    'handygate',
    'frame analysis',
    'discourse',
    ]

bio_medical_engineering = [  # complete
    'medical exercise therapy',
    'medical training therapy',
    'heart rate',
    'rppg',
    'e health',
    'e rehabilitation',
    'health care',
    'human skeleton',
    'physical training',
    'point of common coupling',
    'behaviour analysis',
    'stereo vision',
    'automatic fall detection',
    'people detection',
    'elderly care',
    'motion quality assessment',
    'machine learning',
    'skeleton normalisation',
    'motion analysis',
    'realtime feedback',
    'hip osteoarthritis',
    'hip arthroplasty',
    'cable pulley machine',
    'care situation',
    'degrees of freedom of movement',
    'motion sequence matching',
    'incremental dynamic time warping',
    'medical tracking',
    'micromotors',
    'photoacoustics',
    'ultrasound',
    'vivo imaging',
    'microrobots',
    'targeted therapy',
    'target monitoring',
    'swarm tracking',
    'tissues',
    'phantoms',
    'optoacoustic imaging',
    'optimal motor',
    'nanoparticles',
    'micro',
    'cells',
    'implantable biomedical',
    'enzyme',
    'biocatalysts',
    'glucose',
    'dehydrogenase',
    'nanomembranes',
    'magnetic field sensors',
    'nanoscale',
    'nanomaterials',
    'graphene oxide',
    'biomedical application',
    'physiological processes',
    'patient or medical doctor',
    'microfluidics',
    'bacteria detection',
    'impedance spectroscopy',
    'gait analysis',
    'polydimethylsiloxane',
    'disease prevention',
    'feature extraction',
    'energy management',
    'boost converter',
    'medical instrumentation',
    'howland configuration',
    'biomedical devices',
    'bioimpedance',
    'spectroscopy',
    'ultrasonic sensors',
    'stair recognition',
    'medical application',
    'transurethral resection',
    'stimulator',
    'embedded systems',
    'gradiometer',
    'sensoren',
    'medizinische',
    'messtechnik',
    'bipolar electrosurgery',
    'spatial resolution',
    'visualisation',
    'electrosurgery',
    'tur',
    'medizinische technik',
    'potential distribution',
    'bioelectric potentials',
    'data acquisition',
    'surgery',
    'telemetry',
    'biomedical networking and communication',
    'wsn',
    'eeg',
    'ecg',
    'ergospirometry',
    'epilepsy',
    'medizinische messtechnik',
    'medical systems',
    'electro chemistry',
    'corrosion',
    'energy harvesting',
    'medical engineering',
    'moems',
    'manometry',
    'fiber bragg grating',
    'medical devices',
    'gastrointestinal',
    'mems',
    'medical rehabilitation',
    'health management',
    'neurological practitioner',
    'behavior change',
    'tobacco smoking',
    'medical patients',
    'entscheidungsverhalten',
    'medizinische laien decision making behavior',
    'medical laypersons',
    'medical',
    'pflege',
    'palliativ medicin',
    'oct',
    'medical language processing',
    'medical corpus collection',
    'measuring technology',
    'biomedical instrument',
    'medizinger\xc3\xa4te',
    'biomechanics',
    'haptic interfaces',
    'medical computing',
    'micro processing',
    'medizinischer',
    'mwcnt',
    'pdms',
    ' general practioners',
    'medical studendt',
    'oecd panel',
    'medical staff',
    ]

robotics = [  # complete
    'artificial intelligence',
    'optical sensors',
    'micromotors',
    'microrobots',
    'soft robotics',
    'autonomous systems',
    'soft shareable materials',
    'microtechnology',
    'haptics',
    'jet engines',
    'nanorobotics',
    'autonomous',
    'magnetic fields',
    'control systems',
    'magnetic moments',
    'robotics',
    'hyperdimensional',
    'neural network',
    'place recognition',
    'simulation',
    'visual odometry',
    'mapping',
    'spacebot',
    'localization',
    'pose graph',
    'collision avoidance',
    'reactive motions',
    'material recognition',
    'machine learning',
    'proximity sensors',
    'augmented reality',
    'montageplanung',
    'assembly',
    'Assistive devices',
    'human robot interaction',
    'analysis of variance',
    'impedance control',
    'workload',
    'bionics',
    'anthropomorphism',
    'stereotypes',
    'prostheses',
    'social perception',
    'robotik',
    'distributed system',
    'mechanistic models',
    'motor control',
    'computational neuroscience',
    'neurobotics',
    'hand pose tracking',
    'antagonistic actuators',
    'virtuality',
    'robotik',
    'automotive',
    ]

data_science = [
    'data engineering',
    'data wave housing',
    'data mining',
    'data visualization and presentation',
    'statistical analysis',
    'operations related data analysis',
    'market related data analysis',
    'cloud and distributed computing',
    'database management and architecture',
    'machine learning',
    'ml',
    'congnitive computing development',
    'generic object detection',
    'business intelligence',
    'data science',
    'big data',
    'social media analytics',
    'decision support systems',
    'curriculum design',
    'pedagogy',
    'network science',
    'urban science',
    'complex networks',
    'scientific computing',
    'social computing',
    'datadriven innovation',
    'cluster',
    ]

three_d_models = [  # complete
    'point cloud',
    'cloud point',
    'pount cloud',
    'laserscanner',
    'robotics',
    'tracking',
    'clustering',
    'segmentation',
    'sensor',
    'sensing',
    'detection',
    ]

automation_technology = [  # complete
    'sensor',
    'tracking',
    'robotics',
    'machine learning',
    'iot',
    'internet of things',
    'smart home',
    'optical sensors',
    'microcontrollers',
    'smart cities',
    'automotive',
    ]

internet_of_things = [  # complete
    'internet of thing',
    'internet of things',
    'web of things',
    'things to cloud',
    'virtual prototyping',
    'iot',
    'design process',
    'smart home',
    'smart sensing',
    'visual impairment',
    'data Privacy',
    'smart building',
    'natural language',
    'industrail',
    'digital transformation',
    'rfid',
    'power efficiency',
    'rssi',
    'fingerprinting',
    'medium access control',
    'reliability',
    'voice interface',
    'semantic web',
    'ontology',
    'survey',
    'linked data',
    'case study',
    'design process',
    'hci',
    'human computer interaction',
    'elsi',
    'implications',
    'wireless sensor network',
    'tracking',
    'sensor',
    'amazon web',
    'implications',
    'undersampling',
    'embedded system',
    'spectroscopy',
    'voltage sensor',
    'sql',
    'wsns',
    ]

micro_controller = [  # complete
    'jet',
    'pja',
    'laserdisplay',
    'laser',
    'moems',
    'scannpattern',
    'actuators',
    'control',
    'micro forming',
    'haptics',
    'robotics',
    'microtechnology',
    'robotics',
    'measurement',
    'microtechnology',
    'magnetic field',
    'microrobot',
    'magnetic control',
    'microtube',
    'motile cell',
    'active flow control',
    'micro waves',
    'integration',
    'microcarriers',
    'pulsed jet actuator',
    'technology',
    'electrical',
    'machining',
    'jet',
    'wireless sensor',
    'sensor node',
    'energy optimization',
    'microscale systems',
    'polymeric stracture',
    'remote controle',
    'micromachine',
    'nanomachine',
    ]

embedded_systems = [  # complete
    'bioimpedance spectroscopy',
    'excitation signal',
    'spectral energy efficiency',
    'crest Factor',
    'embedded Systems',
    'real implementation',
    'timer',
    'medical devices',
    'mobility',
    'measurement methods',
    'battery',
    'signal processing',
    'automative sensors',
    'iir',
    'dsp',
    'bms',
    'rasberry pi',
    'operating system',
    'software testing',
    'development process',
    'wireless',
    'hardware',
    'computer science',
    ]

distributed_systems = [  # complete
    'autosar',
    'middleware',
    'container',
    'distributed systems',
    'smart grid',
    'distributed optimization',
    'optimal power flow',
    'distributed energy resources',
    'software architecture',
    'barrelfish',
    'distributed active objects',
    'mobility',
    'python',
    'distributed system',
    'mobility awareness',
    'distributed operating system',
    'distributed processing',
    'computational modeling',
    'multimedia information retrieval',
    'workflow optimization',
    'workflow',
    'image recognition',
    'tracking methods',
    'machine learning',
    'distributed infrastructure',
    'distributed algorithms',
    'data redistribution',
    'particle simulations',
    'message passing',
    'distributed memory',
    'data redistribution',
    'distributed simulations',
    'scheduling methods',
    'fem simulations',
    'data coupling',
    'scientific computing',
    'engineering simulation',
    'numerical simulations',
    'injection molding',
    'optimization',
    'parallel computing',
    'networking',
    'task graph',
    'optimization algorithm',
    'scheduling software',
    'software engineering',
    'cloud computing',
    'architectural analysis',
    'distributed infrastructure',
    'wireless',
    'distributed embedded systems',
    'verteilte systeme',
    'rcc',
    'specification of layers',
    'embedded systems',
    'distributed displays',
    'widgets',
    'web applications',
    'distributed user interfaces',
    'distributed user interface',
    'composition',
    'reusability',
    'web of things',
    'html5',
    'distributed search',
    'distraction',
    'distributed production',
    'distributed fibre direction',
    'distributed actuators',
    'integrated actuators',
    'decentralization',
    'subgradient methods',
    'blockchain',
    'distributed cognition',
    'analogy',
    'management of knowledge and innovation',
    'distributed energy supply',
    ]

agile_development = [  # complete
    'software migration',
    'prototyping',
    'modeldriven developmen',
    'api',
    'agile development',
    'portfolio management',
    'business process management',
    'scrum',
    'development process',
    'sme',
    'agile method',
    'agiles',
    'inclusive business',
    'agile business intelligence',
    'bi agility',
    'automated testing',
    'regression testing',
    'agile values',
    'agile principles',
    'agile analytics',
    'web engineering',
    ]
    
mems = [  # complete
    'mems',
    'vhdl',
    'cnt',
    'fem',
    'cfd',
    'tpwl',
    'avt',
    'ae',
    'bandpass',
    'simulation',
    'mechanics',
    'rom',
    'moems',
    'sensor',
    'af detection',
    'quqntam dots',
    'rfid interface',
    'filter monitoring',
    'sigma delta adc',
    'design automation',
    'lightweight integration',
    'acoustic emission',
    'heart frequency measurement',
    'pulse frequency measurement',
    'pulse wave',
    'system modeling',
    'thermal actuator',
    'nanomaterial',
    'gyroscope',
    'quality factor',
    'reliability',
    'metaldetector',
    'laser',
    ]


# get maximum appeared tags with subject

def maximum_rating_number(text, subject):
    index = 0
    count = 0

    # print("INNNER")

    for research_area in range(len(subject)):
        if re.search((str(subject[index]).lower()), text):
            count = count + 1
            index = index + 1
        else:

            # print(subject[index])
            # print(range(len(subject)))

            index = index + 1

    # print(text)
    # print(subject)

    if count != 0 or count != None:
        return count


row_list = []
for i in range(len(df)):
    authors = df.loc[i, 'Authors']
    modify_authors = df.loc[i, 'authors_modify']

    title = df.loc[i, 'Title']
    modify_title = df.loc[i, 'title_modify']

    areas = df.loc[i, 'research_area_clean']
    modify_areas = df.loc[i, 'research_area_modify']

    year = df.loc[i, 'Year']
    source = df.loc[i, 'Source']
    link = df.loc[i, 'Link']
    pub_type = df.loc[i, 'Publication Type']
    flag = 1

   # subjects 15

    area01_web_engineering = maximum_rating_number(areas,
            web_engineering)  # web engineering *complete
    area02_cloud_computing = maximum_rating_number(areas,
            cloud_computing)  # cloud computing *complete
    area_03_information_retrieval = maximum_rating_number(areas,
            information_retrieval)  # information retrieval *complete
    area_04_deep_learning = maximum_rating_number(areas, deep_learning)  # deep learning *complete
    area_05_big_data = maximum_rating_number(areas, big_data)  # big data *complete
    area_06_bio_medical_engineering = maximum_rating_number(areas,
            bio_medical_engineering)  # bio medical engineering *complete
    area_07_robotics = maximum_rating_number(areas, robotics)  # robotics *complete
    area_08_data_science = maximum_rating_number(areas, data_science)  # data science *complete
    area_09_three_d_models = maximum_rating_number(areas,
            three_d_models)  # three d models *complete
    area_10_automation_technology = maximum_rating_number(areas,
            automation_technology)  # automation technology
    area_11_internet_of_things = maximum_rating_number(areas,
            internet_of_things)  # internet of things(iot) *complete
    area_12_micro_controller = maximum_rating_number(areas,
            micro_controller)  # micro controller *complete
    area_13_embedded_systems = maximum_rating_number(areas,
            embedded_systems)  # embedded_systems *complete
    area_14_distributed_systems = maximum_rating_number(areas,
            distributed_systems)  # distributed_systems *complete
    area_15_agile_development = maximum_rating_number(areas,
            agile_development)  # agile_development *complete
    area_16_mems = maximum_rating_number(areas,
            mems)  # mems *complete

   # all subject list with max tags number

    max_list = [
        area01_web_engineering,
        area02_cloud_computing,
        area_03_information_retrieval,
        area_04_deep_learning,
        area_05_big_data,
        area_06_bio_medical_engineering,
        area_07_robotics,
        area_08_data_science,
        area_09_three_d_models,
        area_10_automation_technology,
        area_11_internet_of_things,
        area_12_micro_controller,
        area_13_embedded_systems,
        area_14_distributed_systems,
        area_15_agile_development,
        area_16_mems,
        ]

    max_value = max(max_list)  # get the subject of area
    print("Max Value : "+str(max_value))

    if max_value != 0:  # for empty research field or no match
        if max_list.index(max_value) == 0:  # web engineering
            tags = 'web engineering'
            if re.search('(cloud computing | computing cloud | computing)'
                         , str(areas)):
                tags = tags
            else:
                tags = 'cloud computing' + '|' + tags

            if re.search('(iot | internet of thing)', str(areas)):
                tags = tags
            else:
                tags = 'internet of things (iot)' + '|' + tags

            if re.search('dbms | database | database management',
                         str(areas)):
                tags = tags
            else:
                tags = 'database management (dbms)' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 1:

                                             # cloud computing

            tags = 'cloud computing'
            if re.search('(automative | automation)', str(areas)):
                tags = 'automation technology' + '|' + tags
            else:
                tags = tags

            if re.search('(point clouds | point cloud | pount cloud)',
                         str(areas)):
                tags = '3d visualization' + '|' + tags
            else:
                tags = tags

            if re.search('(big data | data)', str(areas)):
                tags = 'data science' + '|' + tags
            else:
                tags = tags

            if re.search('(health)', str(areas)):
                tags = 'bio medical' + '|' + tags
            else:
                tags = tags

            if re.search('(iot| internet of thing | internet of things)'
                         , str(areas)):
                tags = tags
            else:
                tags = 'internet of things (iot)' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 2:

                                                # information retrieval

            tags = 'information retrieval'
            if re.search('(iot| internet of thing | internet of things)'
                         , str(areas)):
                tags = tags
            else:
                tags = 'internet of things (iot)' + '|' + tags

            if re.search('(media encoding | media retrieval)',
                         str(areas)):
                tags = tags
            else:
                tags = 'media encoding' + '|' + tags
            if re.search('(automated | automation)', str(areas)):
                tags = tags
            else:
                tags = 'automation technology' + '|' + tags
            if re.search('business intelligence|intelligence|business|information'
                         , str(areas)):
                tags = 'intelligent information management' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 3:

                                             # deep learning

            tags = 'deep learning'
            if re.search('machine learning', str(areas)):
                tags = tags
            else:
                tags = 'machine learning' + '|' + tags
            if re.search('data science', str(areas)):
                tags = tags
            else:
                tags = 'data science' + '|' + tags
            if re.search('artificial', str(areas)):
                tags = tags
            else:
                tags = 'artificial intelligence' + '|' + tags
            if re.search('(cnn|ann|classification)', str(areas)):
                tags = 'neural network algorthium' + '|' + tags
            else:
                tags = tags
            if re.search('(raspberry pi|raspberry|pi)', str(areas)):
                tags = 'internet of things (iot)' + '|' + tags
            else:
                tags = tags
            if re.search('(extraction|detection|recognition|processing|information)'
                         , str(areas)):
                tags = 'pattern recognition' + '|' \
                    + 'information retrieval' + '|' + tags
            else:
                tags = tags
            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 4:

                                             # big data

            tags = 'big data'
            if re.search('machine learning | data science | data mining | data'
                         , str(areas)):
                tags = tags
            else:
                tags = 'data science' + '|' + tags
            if re.search('iot | internet of things | internet of thing | wireless'
                         , str(areas)):
                tags = 'automation technology' + '|' + tags
            else:
                tags = tags
            if re.search('(extraction|detection|recognition|processing|information)'
                         , str(areas)):
                tags = 'pattern recognition' + '|' \
                    + 'information retrieval' + '|' + tags
            else:
                tags = tags
            if re.search('(cnn|ann|classification|adaboost|knn)',
                         str(areas)):
                tags = 'neural network algorthium' + '|' + tags
            else:
                tags = tags
            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 5:

                                             # bio medical engineering

            tags = 'bio medical engineering'
            if re.search('micro robots|microrobots|robots|robotics|micromotors'
                         , str(areas)):
                tags = 'robotics' + '|' + tags
            else:
                tags = tags
            if re.search('tracking|sensors|automatic', str(areas)):
                tags = 'automation technology' + '|' + tags
            else:
                tags = tags
            if re.search('enzyme|glucose|dehydrogenose|nanomembranes|graphene oxide|biomedical application'
                         , str(areas)):
                tags = 'bio informatics' + '|' + tags
            else:
                tags = tags
            if re.search('data acquisition', str(areas)):
                tags = 'information retrieval' + '|' + tags
            else:
                tags = tags
            if re.search('machine learing', str(areas)):
                tags = 'data science' + '|' + tags
            else:
                tags = tags
            if re.search('(extraction|detection|recognition|processing)'
                         , str(areas)):
                tags = 'pattern recognition' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 6:

                                             # robotics

            tags = 'robotics'
            if re.search('computational', str(areas)):
                tags = 'data science' + '|' + tags
            else:
                tags = tags
            if re.search('sensor|tracking|wireless|autonomous',
                         str(areas)):
                tags = 'internet of things (iot)' + '|' \
                    + 'automation technology' + '|' + tags
            else:
                tags = tags
            if re.search('recognition|simulation|extraction',
                         str(areas)):
                tags = 'pattern recognition' + '|' + tags
            else:
                tags = tags
            if re.search('machine learning', str(areas)):
                tags = 'neural network algorthium' + '|' + tags
            else:
                tags = tags
            if re.search('artificial', str(areas)):
                tags = tags
            else:
                tags = tags = 'artificial intelligence' + '|' + tags
            if re.search('micro controller', str(areas)):
                tags = tags
            else:
                tags = tags = 'micro controller' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 7:

                                             # data science

            tags = 'data science'
            if re.search('recognition|simulation|extraction|analysis',
                         str(areas)):
                tags = 'pattern recognition' + '|' + tags
            else:
                tags = tags
            if re.search('machine learning|ml', str(areas)):
                tags = 'artificial intelligence' + '|' + tags
            else:
                tags = tags
            if re.search('big data', str(areas)):
                tags = 'deep learning' + '|' + tags
            else:
                tags = tags
            if re.search('database', str(areas)):
                tags = 'web engineering' + '|' + tags
            else:
                tags = tags
            if re.search('information retrieval', str(areas)):
                tags = tags
            else:
                tags = 'information retrieval' + '|' + tags
            if re.search('business intelligence|intelligence|business|information'
                         , str(areas)):
                tags = 'intelligent information management' + '|' + tags
            else:
                tags = tags
            if re.search('business intelligence|intelligence|business|information'
                         , str(areas)):
                tags = 'intelligent information management' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 8:

                                             # 3d visualization

            tags = '3d visualization'
            if re.search('sensor|tracking|detection|segmentation',
                         str(areas)):
                tags = 'internet of things (iot)' + '|' \
                    + 'automation technology' + '|' + tags
            else:
                tags = tags
            if re.search('robotics', str(areas)):
                tags = tags = 'micro controller' + '|' + tags
            else:
                tags = tags
            if re.search('recognition|simulation|extraction|analysis|clustering'
                         , str(areas)):
                tags = 'pattern recognition' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 9:

                                             # automation technology microcontrollers

            tags = 'automation technology'
            if re.search('(internet.*of.*things|iot|internet.*of.*thing)'
                         , str(areas)):
                tags = tags
            else:
                tags = 'internet of things (iot)' + '|' + tags
            if re.search('microcontroller|microcontrollers',
                         str(areas)):
                tags = tags
            else:
                tags = 'robotics' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 10:

                                              # internet of things (iot)

            tags = 'internet of things (iot)'
            if re.search('(cloud| cloud computing)', str(areas)):
                tags = 'cloud computing' + '|' + tags
            else:
                tags = tags
            if re.search('(smart| rfid | fingerprinting | sensor)',
                         str(areas)):
                tags = 'automation technology' + '|' + tags
            else:
                tags = tags
            if re.search('(semantic web| design process | human computer interaction| hci| sql)'
                         , str(areas)):
                tags = 'web engineering' + '|' + tags
            else:
                tags = tags
            if re.search('business intelligence|intelligence|business|information'
                         , str(areas)):
                tags = 'intelligent information management' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 11:

                                              # micro controller

            tags = 'micro controller'
            if re.search('(iot| internet of thing)', str(areas)):
                tags = tags
            else:
                tags = 'internet of things (iot)' + '|' + tags
            if re.search('robotics', str(areas)):
                tags = tags
            else:
                tags = 'robotics' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 12:

                                              # embedded_systems

            tags = 'embedded systems'
            if re.search('(rasberry| rasberry pi|wireless|automative sensors)'
                         , str(areas)):
                tags = 'internet of things (iot)' + '|' \
                    + 'micro controller' + '|' + tags
            else:
                tags = tags
            if re.search('software testing|operating system|computer science|development process'
                         , str(areas)):
                'web engineering' + '|' + tags
            else:
                tags = 'robotics' + '|' + tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 13:

                                              # distributed_systems

            tags = 'distributed systems'
            if re.search('wireless|sensor|automatic', str(areas)):
                tags = 'internet of things (iot)' + '|' + tags
            else:
                tags = tags
            if re.search('web', str(areas)):
                tags = 'web engineering' + '|' + tags
            else:
                tags = tags
            if re.search('robotics|robotik', str(areas)):
                tags = 'micro controller' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 14:

                                              # agile_development

            tags = 'agile development'
            if re.search('web|software', str(areas)):
                tags = 'web engineering' + '|' + tags
            else:
                tags = tags
            if re.search('business intelligence|intelligence|business',
                         str(areas)):
                tags = 'intelligent information management' + '|' + tags
            else:
                tags = tags
            if re.search('data', str(areas)):
                tags = 'data science' + '|' + tags
            else:
                tags = tags

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': tags,
                }
            row_list.append(dict1)
        elif max_list.index(max_value) == 15:

                                              # mems

            tags = 'micro-electromechanical systems'
            if re.search('rfid|sensor', str(areas)):
                tags = 'internet of things (iot)' + '|' + tags
            else:
                tags = tags
        else:

            dict1 = {
                'Title': modify_title,
                'Authors': modify_authors,
                'Research Area': modify_areas,
                'Year': year,
                'Publication Type': pub_type,
                'Source': source,
                'Link': link,
                'TAG': 'none',
                }
            row_list.append(dict1)
    else:

        dict1 = {
            'Title': modify_title,
            'Authors': modify_authors,
            'Research Area': modify_areas,
            'Year': year,
            'Publication Type': pub_type,
            'Source': source,
            'Link': link,
            'TAG': 'none',
            }
        row_list.append(dict1)

# insert the new list in dataframe   ....

df2 = pd.DataFrame(row_list)

# get the unique values (rows)

df2 = df2.drop_duplicates(subset=['Title'])

# print(df2)

df2.to_csv('processed_tagsV1.csv')

# split sentences
# def sentences(text):
    # split sentences and questions
    # text = re.split(' ', text)
    # clean_sent = []
    # for sent in text:
        # clean_sent.append(sent)'''
    # print(clean_sent)
    # return clean_sent

# sentences
# df['RA'] = df['research_area_clean'].apply(sentences)
# print(df['RA'])

# create a dataframe containing sentences
# df2 = pd.DataFrame(columns=['RA','Year'])

# row_list = []

# for i in range(len(df)):
    # for sent in df.loc[i,'RA']:

        # wordcount = len(sent.split())
        # year = df.loc[i,'Year']

        # dict1 = {'Year':year,'RA':df.loc[i,'RA'],'Len':wordcount}
        # row_list.append(dict1)'''
        # print(row_list)

# df2 = pd.DataFrame(row_list)

# row_list = []
# pattern = ['Cloud computing', 'Event-driven', 'Micro-services', 'Kafka', 'Wireless sensor network', 'Internet of things', 'Amazon web service', 'IoT']
# for i in range(len(df)):
   # year = df.loc[i,'Year']
   # pub_type = df.loc[i,'Publication Type']
   # text_ = df.loc[i,'RA']'''
   # print(text_)
   # flag = 1
   # for area in text_:
       # r = re.compile(r'\bcloud\b | \bcomputing\b | \bwireless\b', flags=re.I | re.X)
       # print(text_[area])

       # if((r.findall(area)) and flag ==1):
           # dict1 = {'Year':year,'RA':df.loc[i,'RA'],'PT':pub_type, 'TAG': 'Information Retrieval'}
           # row_list.append(dict1)
           # flag= 0'''
       # elif(re.search("^*.cloud computing.$*", str(area)) and flag ==1):
           # dict1 = {'Year':year,'RA':df.loc[i,'RA'],'PT':pub_type, 'TAG': 'Web internet'}
           # row_list.append(dict1)
           # flag= 0
           # print(row_list)
   # dict1 = {'Year':year,'RA':df.loc[i,'RA'],'PT':pub_type}
   # row_list.append(dict1)
   # if(re.search(pattern, str(text_))):
       # df['tag'] = 'information retrieval'
        # dict1 = {'Year':year,'RA':df.loc[i,'RA'],'PT':pub_type, 'TAG': 'information retrieval'}
        # row_list.append(dict1)
        # print(row_list)'''

# df2 = pd.DataFrame(row_list)
# print(df2['TAG'])

