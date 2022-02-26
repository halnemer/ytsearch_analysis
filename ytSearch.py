from googleapiclient.discovery import build
from pandas import *


URL = 'https://www.googleapis.com/youtube/v3/search'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

## publish date, video title, url, channel, num of views, num of likes, num of dislikes
titleList = []
urlList = []
viewsList = []
publishTimeList = []
tagsList = []
videoIdList = []
likesList = []
commentsCountList = []

# def menu():
# 	print("Hi ...")
# 	region_code = input("Enter the region code: ")
# 	searchWords = input("Search: ")

# def main():
# 	searchWord = input("Search: ")
# 	searchEngine(searchWord)

def searchDetails():
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

	requestSearch = youtube.search().list(
			part='snippet',
			q="japan",
			type='video',
			maxResults=100,
			regionCode = "jp"
		)

	searchResult = requestSearch.execute()

	# print(searchResult["items"][0]["id"]["videoId"])

	for video in searchResult['items']:
		titleList.append(video["snippet"]["title"])
		urlList.append("https://www.youtube.com/watch?v=" + video["id"]["videoId"])

		publishTimeList.append(video["snippet"]["publishedAt"])
		print(video["snippet"]["title"])
		print("https://www.youtube.com/watch?v=" + video["id"]["videoId"])
		videoDetails(video["id"]["videoId"])
	# dict = {
	# 	"published Date": publishTimeList,
	# 	"titles": titleList,
	# 	"url": urlList,
	# }
	# df = DataFrame(dict)

	# print(df)
	# print(titleList)
	# print(urlList)

	# print(result['items'][0]["id"]["videoId"])


def videoDetails(ID):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
	# for ID in videoIdList:
	videoInfoRequest = youtube.videos().list(
		part="statistics, snippet",
		id=ID
	)

	response = videoInfoRequest.execute()
	print(response["items"][0]["statistics"]["viewCount"])
	print()
	viewsList.append(response["items"][0]["statistics"]["viewCount"])
	likesList.append(response["items"][0]["statistics"]["likeCount"])
	commentsCountList.append(response["items"][0]["statistics"]["commentCount"])
		# break

if __name__ == '__main__':
	searchDetails()


# {'kind': 'youtube#searchResult', 'etag': 'ASbYD4MD6-BrWoE0Oxc32pqzNm4', 'id': {'kind': 'youtube#video', 'videoId': 'EIasjOqBLtk'}, 'snippet': {'publishedAt': '2022-01-26T11:07:21Z', 'channelId': 'UCjKgO1L27PHXPRp85IRRkKg', 'title': 'WTF Moments in Football #40', 'description': 'Buy discount football jerseys 21/22 at https://www.sen31.ru ⏺ Use the code “SAVE20” to get a 20% off ⚽ My Football videos ...', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/EIasjOqBLtk/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/EIasjOqBLtk/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/EIasjOqBLtk/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': 'SEN31 Extra', 'liveBroadcastContent': 'none', 'publishTime': '2022-01-26T11:07:21Z'}}
