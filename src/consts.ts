type Config = {
  title: string;
  description: string;
  lang: string;
  profile: {
    author: string;
    description?: string;
  }
}

type SocialLink = {
  icon: string;
  friendlyName: string; // for accessibility
  link: string;
}

export const siteConfig: Config = {
  title: "kwertyops",
  description: "",
  lang: "en-GB",
  profile: {
    author: "Andrew Hannum",
    description: "professor of cs ⋅ musician"
  }
}

/** 
  These are you social media links. 
  It uses https://github.com/natemoo-re/astro-icon#readme
  You can find icons @ https://icones.js.org/
*/
export const socialLinks: Array<SocialLink> = [
  {
    icon: "mdi:github",
    friendlyName: "Github",
    link: "https://github.com/kwertyops",
  },
  {
    icon: "mdi:linkedin",
    friendlyName: "LinkedIn",
    link: "https://www.linkedin.com/in/andrew-hannum-24488058/",
  },
  {
    icon: "ri:bluesky-fill",
    friendlyName: "Bluesky",
    link: "https://bsky.app/profile/kwertyops.bsky.social",
  },
  {
    icon: "mdi:email",
    friendlyName: "email",
    link: "mailto:andrew.hannum@gmail.com",
  },
  {
    icon: "mdi:rss",
    friendlyName: "rss",
    link: "/rss.xml"
  }
];

export const NAV_LINKS: Array<{ title: string, path: string }> = [
  {
    title: "Home",
    path: "/",
  },
  // {
  //   title: "About",
  //   path: "/about",
  // },
  {
    title: "Music",
    path: '/music'
  },
  {
    title: "Clippings",
    path: '/clipping'
  },
  {
    title: "Feed",
    path: "/blog",
  },
  {
    title: "Projects",
    path: '/projects'
  },
  // {
  //   title: "Archive",
  //   path: '/archive'
  // }
];
