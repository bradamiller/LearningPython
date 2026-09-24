/**
 * Remark plugin: number the <Todo> elements in each lesson, in document order.
 *
 * The note itself carries no id, so there is nothing for /todos to link to.
 * Rather than hand-write an id on all 29 notes (and keep them unique forever),
 * this stamps an `index` prop on each one at build time and <Todo> renders it
 * as `id="todo-<index>"`.
 *
 * scripts/extract_todos.js counts the same way over the same source, so item
 * N in the index is element #todo-N on the page. THE TWO MUST AGREE: if you
 * change the ordering or the matching here, change it there too, or every link
 * on the index page lands one note off.
 *
 * Runs before the strip plugin does its work; in a SHOW_TODOS=0 build the
 * numbered nodes are deleted anyway, and the index is emitted empty to match.
 *
 * Dependency-free on purpose, matching remark-strip-todos.js.
 */
export default function remarkNumberTodos() {
  return (tree) => {
    let n = 0;
    const walk = (node) => {
      if (!Array.isArray(node.children)) return;
      for (const child of node.children) {
        const isTodo =
          (child.type === 'mdxJsxFlowElement' ||
            child.type === 'mdxJsxTextElement') &&
          child.name === 'Todo';
        if (isTodo) {
          n += 1;
          child.attributes = child.attributes || [];
          child.attributes.push({
            type: 'mdxJsxAttribute',
            name: 'index',
            value: String(n),
          });
        }
        walk(child);
      }
    };
    walk(tree);
  };
}
