{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 audio_file_folder_name = '5_speakers_audio_data_3sec'\
\
def generate_mfcc(intial_directory, final_directory, no_of_coefficients):\
    for file in os.listdir(os.path.join(initial_directory,audio_file_folder_name)):\
        \
        filepath = initial_directory+'/'+audio_file_folder_name+'/'+file;\
        mfcc_image_prefix = os.path.splitext(os.path.basename(file))[0]\
        #filepath = os.path.join(initial_directory, audio_file_folder_name, file);\
        print("Currently processing ", file)\
\
        y, sr = librosa.load(filepath)\
        mfccs = librosa.feature.mfcc(y, n_mfcc = no_of_coefficients, sr = sr)\
        #plt.figure(figsize = (25,10))\
        librosa.display.specshow(mfccs, x_axis = 'time', sr = sr)\
        fig = plt.gcf()\
        for i, mfccs in enumerate(mfccs):\
            \
            fig.savefig(final_directory+"/"+mfcc_image_prefix+'.jpg')}