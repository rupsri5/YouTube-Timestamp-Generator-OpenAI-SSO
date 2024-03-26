from youtube_transcript_api import YouTubeTranscriptApi
from app.openai_helper.chains import ChainFactory
from app.openai_helper.models import GPT_4, GPTConfig
from app.openai_helper.utility import make_openai_call

def format_duration(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    formatted_duration = f"{minutes:02}:{remaining_seconds:02}"

    return formatted_duration


def extract_transcript_from_youtube(youtube_link):
    # Generate an array of transcripts.
    video_id = youtube_link.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    ### Currently, we are utilizing a free OpenAI key that restricts us to a maximum of two concurrent calls.
    ### Currently, we are employing a sequential call that requires 70 seconds to generate for a 10-minute video. 
    output_list=[]
    for i in range(0,len(transcript),30):
        end_index=i+30 if i+30<len(transcript) else len(transcript)
        # structured_data.append({"transcript":transcript[i:end_index]})
        output= ChainFactory().timestamp_chain().run(transcript=transcript[i:end_index])
        output_list.append(output)
        
    ### Using a paid OpenAI key allows us to make parallel calls, which typically take 4-5 seconds to process.
    ### Below is the code for making parallel calls using a paid OpenAI key.
    # structured_data=[]
    # for i in range(0,len(transcript),30):
    #     end_index=i+30 if i+30<len(transcript) else len(transcript)
        # structured_data.append({"transcript":transcript[i:end_index]})
    # output_list = make_openai_call(structured_data,ChainFactory(config=GPTConfig(model=GPT_4)).timestamp_chain())


    # Format output
    output_text_list=[]
    for output_json in output_list:
        output_json = eval(output_json)
        for key in output_json.keys():
            output_text_list.append(f"{format_duration(int(output_json[key]))} || {key}")

    return output_text_list
