{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww28600\viewh18000\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 dataset_folder_name = '5_speakers_audio_data'\
def split_audio_file(initial_directory, final_directory, duration):#enter duration in milliseconds\
    for folder in os.listdir(os.path.join(initial_directory,dataset_folder_name)):\
        for file in os.listdir(os.path.join(initial_directory,dataset_folder_name,folder)):\
            \
            filepath = os.path.join(initial_directory, '5_speakers_audio_data', folder, file);\
            filename_prefix = os.path.splitext(os.path.basename(file))[0]\
            myaudio = AudioSegment.from_file(filepath, "wav") \
            chunk_length_ms = duration # pydub calculates in millisec\
            chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of 3 sec\
\
            #Export all of the individual chunks as wav files\
\
            for i, chunk in enumerate(chunks):\
                chunk_name = final_directory+"/"+filename_prefix+"_chunk\{0\}.wav".format(i)\
                print(chunk_name)\
                chunk.export(chunk_name, format="wav")}