// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'XRP Python Curriculum',
  tagline: 'Learn Python by programming a real robot',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://bradamiller.github.io',
  baseUrl: '/',

  organizationName: 'bradamiller',
  projectName: 'IntoToPython',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // XRP brand typeface (Montserrat), matched to experiential.bot
  stylesheets: [
    'https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap',
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/', // docs are the site root, like a curriculum
          sidebarPath: './sidebars.js',
          editUrl: undefined,
          showLastUpdateTime: false,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        respectPrefersColorScheme: true,
      },
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      navbar: {
        title: 'XRP Python Curriculum',
        logo: {
          alt: 'XRP Robot',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'curriculumSidebar',
            position: 'left',
            label: 'Curriculum',
          },
          {
            to: '/checks',
            label: 'Printable Checks',
            position: 'left',
          },
          {
            href: 'https://xrpcode.wpi.edu/',
            label: 'XRP Code IDE',
            position: 'right',
          },
          {
            href: 'https://github.com/bradamiller/IntoToPython',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Course',
            items: [
              {label: 'Module 1: Driving', to: '/module-01-driving/lesson-01-meet-the-xrp'},
            ],
          },
          {
            title: 'Resources',
            items: [
              {label: 'XRP Code IDE', href: 'https://xrpcode.wpi.edu/'},
              {label: 'XRP User Guide', href: 'https://xrpusersguide.readthedocs.io/'},
              {label: 'Support Forum', href: 'https://xrp.discourse.group/'},
            ],
          },
        ],
        copyright: `XRP Python Curriculum · Built for high school classrooms.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['python'],
      },
    }),
};

export default config;
