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
    description: "your bio description"
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
    link: "https://github.com/kirontoo/astro-theme-cody",
  },
  {
    icon: "mdi:linkedin",
    friendlyName: "LinkedIn",
    link: "#",
  },
  {
    icon: "mdi:email",
    friendlyName: "email",
    link: "mailto:ndangamy@gmail.com",
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
  {
    title: "About",
    path: "/about",
  },
  {
    title: "Blog",
    path: "/blog",
  },
  {
    title: "Music",
    path: '/music'
  },
  {
    title: "Clippings",
    path: '/clippings'
  },
  {
    title: "Projects",
    path: '/projects'
  },
  {
    title: "Archive",
    path: '/archive'
  }
];
