import pyperclip
from fuzzywuzzy import process
import sys
import os
import time

# Try 2 Collect all the link that we can
def generate_social_links(username):
    return {
        "Facebook": f"https://facebook.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}",
        "YouTube": f"https://youtube.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Stack Overflow": f"https://stackoverflow.com/users/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dev.to": f"https://dev.to/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Behance": f"https://behance.net/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",
        "Quora": f"https://www.quora.com/profile/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Goodreads": f"https://goodreads.com/{username}",
        "Product Hunt": f"https://www.producthunt.com/@{username}",
        "Discord": f"https://discord.com/users/{username}",
        "Telegram": f"https://t.me/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "VK": f"https://vk.com/{username}",
        "Xing": f"https://www.xing.com/profile/{username}",
        "Flickr": f"https://flickr.com/people/{username}",
        "Meetup": f"https://meetup.com/members/{username}",
        "AngelList": f"https://angel.co/{username}",
        "Houzz": f"https://houzz.com/user/{username}",
        "Ello": f"https://ello.co/{username}",
        "Myspace": f"https://myspace.com/{username}",
        "ReverbNation": f"https://reverbnation.com/{username}",
        "Wattpad": f"https://www.wattpad.com/user/{username}",
        "Patreon": f"https://patreon.com/{username}",
        "Ko-fi": f"https://ko-fi.com/{username}",
        "CashApp": f"https://cash.app/${username}",
        "OnlyFans": f"https://onlyfans.com/{username}",
        "Mastodon": f"https://mastodon.social/@{username}",
        "Plurk": f"https://www.plurk.com/{username}",
        "Letterboxd": f"https://letterboxd.com/{username}",
        "Venmo": f"https://venmo.com/{username}",
        "Kik": f"https://kik.me/{username}",
        "Bumble": f"https://bumble.com/{username}",
        "OkCupid": f"https://www.okcupid.com/profile/{username}",
        "Tinder": f"https://tinder.com/{username}",
        "Ravelry": f"https://ravelry.com/people/{username}",
        "Untappd": f"https://untappd.com/user/{username}",
        "Gaia Online": f"https://www.gaiaonline.com/profiles/{username}",
        "Academia.edu": f"https://academia.edu/{username}",
        "ResearchGate": f"https://www.researchgate.net/profile/{username}",
        "Archilovers": f"https://archilovers.com/{username}",
        "Creative Market": f"https://creativemarket.com/{username}",
        "Fiverr": f"https://www.fiverr.com/{username}",
        "Upwork": f"https://www.upwork.com/freelancers/~{username}",
        "PeoplePerHour": f"https://www.peopleperhour.com/freelancer/{username}",
        "500px": f"https://500px.com/{username}",
        "Dailymotion": f"https://dailymotion.com/{username}",
        "Foursquare": f"https://foursquare.com/{username}",
        "LiveJournal": f"https://livejournal.com/{username}",
        "GaiaOnline": f"https://www.gaiaonline.com/profiles/{username}",
        "CafeMom": f"https://www.cafemom.com/{username}",
        "CaringBridge": f"https://www.caringbridge.org/visit/{username}",
        "CafePress": f"https://www.cafepress.com/{username}",
        "Zazzle": f"https://www.zazzle.com/store/{username}",
        "TripAdvisor": f"https://tripadvisor.com/members/{username}",
        "Etsy": f"https://www.etsy.com/people/{username}",
        "Periscope": f"https://www.pscp.tv/{username}",
        "Untappd": f"https://untappd.com/user/{username}",
        "Minted": f"https://www.minted.com/store/{username}",
        "Goodreads": f"https://goodreads.com/{username}",
        "VSCO": f"https://vsco.co/{username}",
        "Instructables": f"https://www.instructables.com/member/{username}",
        "Thingiverse": f"https://www.thingiverse.com/{username}",
        "Polyvore": f"https://www.polyvore.com/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Mix": f"https://mix.com/{username}",
        "Diaspora": f"https://{username}.diasporapod.com",
        "MeWe": f"https://mewe.com/{username}",
        "Minds": f"https://www.minds.com/{username}",
        "Plurk": f"https://www.plurk.com/{username}",
        "AdultFriendFinder": f"https://adultfriendfinder.com/profile/{username}",
        "FetLife": f"https://fetlife.com/users/{username}",
        "Plenty of Fish": f"https://pof.com/{username}",
        "Rumble": f"https://rumble.com/{username}",
        "Gab": f"https://gab.com/{username}",
        "Voat": f"https://voat.co/user/{username}",
        "Minds": f"https://www.minds.com/{username}",
        "BitChute": f"https://www.bitchute.com/channel/{username}",
        "Spreely": f"https://spreely.com/{username}",
        "BrandYourself": f"https://brandyourself.com/{username}",
        "Branded.me": f"https://branded.me/{username}",
        "About.me": f"https://about.me/{username}",
        "Ello": f"https://ello.co/{username}",
        "Yubo": f"https://yubo.live/{username}",
        "Peeks": f"https://peeks.com/{username}",
        "Shapr": f"https://www.shapr.co/profiles/{username}",
    }


def display_page(links, page=0, items_per_page=10):
    """Display the current page of social links."""
    total_pages = (len(links) - 1) // items_per_page + 1
    start = page * items_per_page
    end = start + items_per_page

    print("\nThe Spider Web of Words (Page {}/{}):".format(page + 1, total_pages))
    for i, (name, url) in enumerate(list(links.items())[start:end], start=1):
        print(f"{start + i}. {name}")

    print("""\nSpeak the number, and the web will give you its thread.
      [--] 'L' for the next weave, 'H' to retrace your steps.
      [--] 'S' to hunt for a hidden strand, 'Q' to break the web and leave.
      [--] 'Matrixout' You know, you know.
      """)

def main():
  def clear():
    os.system('clear')
  
  username = input("Enter your username: ")
  links = generate_social_links(username)
  links_name = list(links.keys())

  page = 0
  items_per_page = 10
  while True:
      time.sleep(0.2)
      clear()
      display_page(links, page, items_per_page)
      choice = input("\nChoose: ").strip().lower()
      
      if choice == 'l':
          if (page + 1) * items_per_page < len(links):
              page += 1
          else:
              print("The web ends.")
      elif choice == 'h':
          if page > 0:
              page -= 1
          else:
              print("The web unfurls before you.")
      elif choice == 's':
          search_query = input("Search for: ").strip().lower()
          best_match, score = process.extractOne(search_query, links_name)
          threshold = 70
          if score >= threshold:
              url = links[best_match]
              pyperclip.copy(url)
              print(f"Found: {best_match} & URL copied to clipboard!")
          else:
              print("No close match found.")
      elif choice == 'matrixout':
          print("You are Out Of Matrix now :)")
          sys.exit()
      elif choice.isdigit():
          link_index = int(choice) - 1
          if 0 <= link_index < len(links):
              selected_url = list(links.values())[link_index]
              pyperclip.copy(selected_url)
              print(f"URL copied to clipboard: {selected_url}")
          else:
              print("Invalid number. Please select a number from the displayed list.")
      else:
          print("Invalid choice. Use a number, 'l', 'h', 's', or 'matrixout'.")

if __name__ == "__main__":
  main()
