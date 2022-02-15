from youtube_statistics import YTstats 
  
API_KEY = "AIzaSyA-0KfpLK04NpQN1XghxhSlzG-WkC3DHLs"
  
 
channel_id = "UCTv_7SvGIG9ZdlI-EUqLl-w" 
  
yt = YTstats(API_KEY, channel_id) 
yt.get_channel_statistics() 
yt.dump() 