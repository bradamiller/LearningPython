// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';
import remarkStripTodos from './plugins/remark-strip-todos.js';
import remarkNumberTodos from './plugins/remark-number-todos.js';

// Authoring <Todo> notes ship with the site, hidden behind the "Show TODOs"
// switch — the same arrangement teacher notes already use. Build with
// SHOW_TODOS=0 to strip them out entirely (markup and text both) for a release
// where nobody should be able to find them at all:
//
//     SHOW_TODOS=0 npm run build
const STRIP_TODOS = process.env.SHOW_TODOS === '0';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'XRP Python Curriculum',
  tagline: 'Learn Python by programming a real robot',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  // Served at the root of its own subdomain (GitHub Pages custom domain).
  // static/CNAME carries the domain into every deploy; change both together.
  url: 'https://learningpython.bradhouse.com',
  baseUrl: '/',

  organizationName: 'bradamiller',
  projectName: 'LearningPython',

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
          // Numbering must run whatever happens — it gives each <Todo> the id
          // that /todos links to. Stripping, when asked for, then deletes them.
          beforeDefaultRemarkPlugins: STRIP_TODOS
            ? [remarkNumberTodos, remarkStripTodos]
            : [remarkNumberTodos],
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
            to: '/pacing',
            label: 'Pacing Guide',
            position: 'left',
          },
          {
            // Authoring page. Hidden unless "Show TODOs" is on — a tab
            // advertising the course's unfinished bits is not for students.
            // The CSS gate is html[data-todos='on'] in custom.css.
            to: '/todos',
            label: 'TODOs',
            position: 'left',
            className: 'navbar__item--todos',
          },
          {
            href: 'https://xrpcode.wpi.edu/staging',
            label: 'XRP Code IDE',
            position: 'right',
          },
          {
            href: 'https://github.com/bradamiller/LearningPython',
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
              {label: 'XRP Code IDE', href: 'https://xrpcode.wpi.edu/staging'},
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
