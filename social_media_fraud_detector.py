from collections import deque

class SocialMediaFraudDetector:
    def __init__(self, k):
        self.k = k
        self.recent_posts = deque()
        self.post_hashes = set()

    def process_post(self, post):
        # Remove old posts outside K distance
        if len(self.recent_posts) >= self.k:
            old_post = self.recent_posts.popleft()
            self.post_hashes.remove(hash(old_post))

        post_hash = hash(post)

        # Check duplicate
        if post_hash in self.post_hashes:
            print(f"⚠ Fraud Alert: Duplicate content detected -> '{post}'")
        else:
            print(f"✓ Valid Post: '{post}'")

        self.recent_posts.append(post)
        self.post_hashes.add(post_hash)


# Simulated Social Media Events
posts = [
    "Buy Crypto Now!",
    "Follow me for tips",
    "Buy Crypto Now!",
    "Learn Python",
    "Follow me for tips",
    "Free Giveaway",
    "Learn Python"
]

K = 3

detector = SocialMediaFraudDetector(K)

print("=== Social Media Fraud Detector ===\n")

for post in posts:
    detector.process_post(post)