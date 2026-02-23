def analyze_post_engagement(likes_list):
    total_likes = 0

    for likes in likes_list:
        total_likes += likes

    if total_likes >= 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"

    print("Total Likes:", total_likes)
    print("Post Status:", status)
post_likes = [200, 300, 250, 300]
analyze_post_engagement(post_likes)