/**
 * Remark plugin: remove <Todo> elements from lessons in a production build.
 *
 * The <Todo> component already returns null in production, but that is not
 * enough — MDX still compiles the note's text into the JavaScript bundle as
 * the component's children, so the words ship even though nothing renders.
 * Several of these notes say exactly where a lesson's answers are visible,
 * which is the last thing to put in a file a student can fetch.
 *
 * This drops the nodes before they are ever compiled, so the text is not in
 * the build at all. Dependency-free on purpose: it walks the tree itself
 * rather than pulling in unist-util-visit for a three-line filter.
 */
export default function remarkStripTodos() {
  return (tree) => {
    const walk = (node) => {
      if (!Array.isArray(node.children)) return;
      node.children = node.children.filter(
        (child) =>
          !(
            (child.type === 'mdxJsxFlowElement' ||
              child.type === 'mdxJsxTextElement') &&
            child.name === 'Todo'
          ),
      );
      node.children.forEach(walk);
    };
    walk(tree);
  };
}
