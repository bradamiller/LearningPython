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
    'templates',
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
        'module-02-line-tracking/lesson-00-overview',
        'module-02-line-tracking/lesson-01-reflectance-sensor',
        'module-02-line-tracking/lesson-02-drive-to-the-edge',
        'module-02-line-tracking/lesson-03-bounce-driving',
        'module-02-line-tracking/lesson-04-random-turns',
        'module-02-line-tracking/lesson-05-proportional-control',
        'module-02-line-tracking/lesson-06-two-sensor-following',
        'module-02-line-tracking/lesson-07-sensor-functions',
        'module-02-line-tracking/lesson-08-detecting-intersections',
        'module-02-line-tracking/lesson-09-line-tracking-functions',
        'module-02-line-tracking/lesson-10-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 3 · Grid Driving',
      collapsed: true,
      items: [
        'module-03-grid-driving/lesson-00-overview',
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
        'module-04-manhattan/lesson-01-coordinates-and-tuples',
        'module-04-manhattan/lesson-02-lists',
        'module-04-manhattan/lesson-03-the-manhattan-algorithm',
        'module-04-manhattan/lesson-04-naming-and-testing-the-planner',
        'module-04-manhattan/lesson-05-the-challenge-of-turning',
        'module-04-manhattan/lesson-06-driving-the-path',
        'module-04-manhattan/lesson-07-final-project',
      ],
    },
    {
      type: 'category',
      label: 'Module 4 test · Top-down (trial)',
      collapsed: true,
      items: [
        'test-module-04/lesson-00-overview',
        'test-module-04/lesson-01-coordinates-and-tuples',
        'test-module-04/lesson-02-lists',
        'test-module-04/lesson-03-the-main-program',
        'test-module-04/lesson-04-the-planner',
        'test-module-04/lesson-05-the-driver',
        'test-module-04/lesson-06-turning',
        'test-module-04/lesson-07-on-the-robot',
      ],
    },
    {
      type: 'category',
      label: 'Module 5 · Pathfinding Around Obstacles',
      collapsed: true,
      items: [
        'module-05-pathfinding/lesson-00-overview',
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
        'module-06-dijkstra/lesson-01-fewest-steps-isnt-fastest',
        'module-06-dijkstra/lesson-02-weights-in-the-graph',
        'module-06-dijkstra/lesson-03-from-bfs-to-dijkstra',
        'module-06-dijkstra/lesson-04-drive-it',
        'module-06-dijkstra/lesson-05-three-planners-one-harness',
      ],
    },
  ],

  // The teacher guide (docs/teacher-guide/): planning, setup, assessment and
  // design notes that belong to no one lesson. Its own sidebar, reached from the
  // "Teacher Guide" navbar item, so it doesn't sit in the students' lesson list.
  teacherGuideSidebar: [
    'teacher-guide/index',
    'teacher-guide/setting-up',
    'teacher-guide/planning',
    'teacher-guide/assessment',
    'teacher-guide/differentiation',
    'teacher-guide/course-design',
    {
      type: 'category',
      label: 'Sample programs',
      link: {type: 'doc', id: 'teacher-guide/sample-programs/index'},
      collapsed: false,
      items: [
        'teacher-guide/sample-programs/module-1',
        'teacher-guide/sample-programs/module-2',
        'teacher-guide/sample-programs/module-3',
        'teacher-guide/sample-programs/module-4',
        'teacher-guide/sample-programs/module-5',
        'teacher-guide/sample-programs/module-6',
      ],
    },
  ],
};

export default sidebars;
