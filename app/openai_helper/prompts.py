SYSTEM_PROMPT_TIMESTAMP="You are an expert timestamp generator for youtube video using its transcript data"

USER_PROMPT_TIMESTAMP="""
Task: Your job is to generate timestamp JSON where key contains "Subject" and value contains start time in seconds.
Output Note: You job is to generate JSON that can be typecased into python dictionary.

Instruction:
1. You will be provided with transcipt data as list of JSON where `text` key contains what user said in video, `start` key contains video time when text said and `duration` key contains total time take to say that text.
2. Note each timestamp and its subject must be more that 20 sec and less than 1min.
3. timestamp must come in order in output JSON like first 0 then 30 then 80 then 120 and so on

Note: Subject for given timestamp must be professional and not directly copied from input data

########################################
Example Input:
Trancript Data:[{{'text': '[Music]', 'start': 0.51, 'duration': 2.169}},"" {{'text': 'these are two of the most important',""  'start': 1.0,""  'duration': 4.0}},"" {{'text': 'people shaping the future of artificial',""  'start': 2.679,""  'duration': 5.12}},"" {{'text': 'intelligence Sam Alman the CEO of open',""  'start': 5.0,""  'duration': 5.96}},"" {{'text': 'aai the startup behind chat GPT and',""  'start': 7.799,""  'duration': 6.241}},"" {{'text': 'Satia Adela the CEO of Microsoft open',""  'start': 10.96,""  'duration': 5.68}},"" {{'text': "ai's biggest investor they spoke to the",""  'start': 14.04,""  'duration': 4.64}},"" {{'text': 'economists editor and chief about what',""  'start': 16.64,""  'duration': 4.84}},"" {{'text': 'the future of AI really looks', 'start': 18.68, 'duration': 6.28}},"" {{'text': "like Sam let's start with you what are",""  'start': 21.48,""  'duration': 5.559}},"" {{'text': 'the most important capabilities that',""  'start': 24.96,""  'duration': 4.799}},"" {{'text': 'chat GPT will develop in the next year',""  'start': 27.039,""  'duration': 4.24}},"" {{'text': 'the world had like a twoe freak out with',""  'start': 29.759,""  'duration': 5.041}},"" {{'text': 'gp4 right this changes everything AGI is',""  'start': 31.279,""  'duration': 6.041}},"" {{'text': 'coming tomorrow there are no jobs by the',""  'start': 34.8,""  'duration': 4.96}},"" {{'text': 'end of the year and now people are like',""  'start': 37.32,""  'duration': 3.68}},"" {{'text': 'why is it so', 'start': 39.76, 'duration': 2.76}},"" {{'text': 'slow', 'start': 41.0, 'duration': 4.44}},"" {{'text': "um and I love that I think that's a",""  'start': 42.52,""  'duration': 4.6}},"" {{'text': 'great thing about the human spirit that',""  'start': 45.44,""  'duration': 3.959}},"" {{'text': "we always want more and better we've not",""  'start': 47.12,""  'duration': 4.119}},"" {{'text': 'had this where there has been some',""  'start': 49.399,""  'duration': 3.921}},"" {{'text': 'general purpose technology whose',""  'start': 51.239,""  'duration': 5.081}},"" {{'text': 'diffusion happened instantaneously',""  'start': 53.32,""  'duration': 5.48}},"" {{'text': 'everywhere in any place Healthcare and',""  'start': 56.32,""  'duration': 5.48}},"" {{'text': 'education is most to the government span',""  'start': 58.8,""  'duration': 6.8}},"" {{'text': 'you now have right the ability to give',""  'start': 61.8,""  'duration': 6.24}},"" {{'text': 'every student and every citizen of the',""  'start': 65.6,""  'duration': 5.28}},"" {{'text': 'of the globe a better health advis and a',""  'start': 68.04,""  'duration': 4.48}},"" {{'text': 'better personalized tutor you know I',""  'start': 70.88,""  'duration': 2.879}}]
########################################
Example Output:{{"Altman and Nadella discussed in Economist":"0","What’s next for ChatGPT?":"25"}}
########################################
Actual Input:
Trancript Data:{transcript}
########################################
Actual Output:?"""