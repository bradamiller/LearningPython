// @ts-check

/**
 * Curriculum sidebar. Mirrors the module/lesson folder structure.
 * Modules 1-5 are real pages. Module 6 (optional) has an overview page; its
 * lessons arrive as the source curriculum's Module 6 is written.
 * Add a new lesson's doc id here under its module category.
 *
 * @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  curriculumSidebar: [
    'how-this-course-works',
    {
      type: 'category',
      label: 'Module 1 · Learning to Drive',
      collapsed: false,
      items: [
        'module-01-driving/lesson-00-what-is-a-robot',
        'module-01-driving/lesson-01-meet-the-xrp',
        'module-01-driving/lesson-02-drawing-shapes',
        'module-01-driving/lesson-03-introduction-to-functions',
        'module-01-driving/lesson-04-parameters-and-customization',
        'module-01-driving/lesson-05-polygon-function',
        'module-01-driving/lesson-06-differential-drive',
        'module-01-driving/lesson-07-blockly-challenges',
        'module-01-driving/lesson-08-hello-python',
        'module-01-driving/lesson-09-variables-and-expressions',
        'module-01-driving/lesson-10-python-loops',
        'module-01-driving/lesson-11-python-functions',
        'module-01-driving/lesson-12-python-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 2 · Line Tracking',
      collapsed: true,
      items: [
        'module-02-line-tracking/lesson-01-reflectance-sensor',
        'module-02-line-tracking/lesson-02-drive-to-the-edge',
        'module-02-line-tracking/lesson-03-bounce-driving',
        'module-02-line-tracking/lesson-04-random-turns',
        'module-02-line-tracking/lesson-05-proportional-control',
        'module-02-line-tracking/lesson-06-two-sensor-following',
        'module-02-line-tracking/lesson-07-detecting-intersections',
        'module-02-line-tracking/lesson-08-introduction-to-classes',
        'module-02-line-tracking/lesson-09-object-composition',
        'module-02-line-tracking/lesson-10-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 3 · Grid Driving',
      collapsed: true,
      items: [
        'module-03-grid-driving/lesson-01-introduction-to-the-grid',
        'module-03-grid-driving/lesson-02-driving-multiple-intersections',
        'module-03-grid-driving/lesson-03-turning-on-the-grid',
        'module-03-grid-driving/lesson-04-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 4 · Manhattan Navigation',
      collapsed: true,
      items: [
        'module-04-manhattan/lesson-00-overview',
        'module-04-manhattan/lesson-01-coordinates',
        'module-04-manhattan/lesson-02-tuples',
        'module-04-manhattan/lesson-03-lists',
        'module-04-manhattan/lesson-04-the-manhattan-algorithm',
        'module-04-manhattan/lesson-05-manhattan-function',
        'module-04-manhattan/lesson-06-testing-without-a-robot',
        'module-04-manhattan/lesson-07-the-challenge-of-turning',
        'module-04-manhattan/lesson-08-driving-the-path',
        'module-04-manhattan/lesson-09-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 5 · Pathfinding Around Obstacles',
      collapsed: true,
      items: [
        'module-05-pathfinding/lesson-01-grid-as-a-graph',
        'module-05-pathfinding/lesson-02-dictionaries',
        'module-05-pathfinding/lesson-03-bfs-concept',
        'module-05-pathfinding/lesson-04-pathfinding-functions',
        'module-05-pathfinding/lesson-05-compute-bfs-path',
        'module-05-pathfinding/lesson-06-testing-and-swapping',
        'module-05-pathfinding/lesson-07-obstacle-detection',
        'module-05-pathfinding/lesson-08-building-experience',
        'module-05-pathfinding/lesson-09-capstone-project',
      ],
    },
    {
      type: 'category',
      label: "Module 6 · Dijkstra's Algorithm (optional)",
      collapsed: true,
      items: [
        'module-06-dijkstra/lesson-00-overview',
      ],
    },
  ],
};

export default sidebars;
