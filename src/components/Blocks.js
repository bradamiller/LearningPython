import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

/**
 * Real XRP Blockly block images (from the XRP User Guide's Blockly Dictionary).
 * Files live in static/img/blocks/<name>.png.
 *
 * <Block name="straight" /> — inline reference to a block inside a sentence.
 *
 * <BlockProgram blocks={[...]} /> — a stacked program that looks like the real
 * workspace. Each block is a string name, or an object:
 *   { name, note, children }
 * A block WITH children is a C-shaped container (Repeat, If, function def): its
 * children are rendered visually enclosed by a colored bracket that matches the
 * block's category color, the way Blockly wraps contained blocks.
 *
 *   <BlockProgram blocks={[
 *     {name:'wait_for_button_press'},
 *     {name:'repeat', note:'repeat 4 times', children:[
 *       {name:'straight', note:'cm: 30'},
 *       {name:'turn', note:'Deg: 90'},
 *     ]},
 *   ]} />
 */

// Category colors sampled from the real block images.
const CONTAINER_COLORS = {
  repeat: '#549054',
  repeat_while: '#549054',
  count: '#549054',
  for_each: '#549054',
  function_def: '#845490',
  funct_def_with_return: '#845490',
  if_do: '#546c90',
};
function containerColor(name) {
  return CONTAINER_COLORS[name] || '#549054';
}

export function Block({name, alt, height = 26}) {
  const src = useBaseUrl(`/img/blocks/${name}.png`);
  return <img className="blockInline" src={src} alt={alt || `${name} block`} style={{height}} />;
}

/**
 * A real screenshot of a block program captured from XRP Code (preferred over the
 * composed BlockProgram — real screenshots show correct values and exact nesting).
 * Capture the program in XRP Code, drop the PNG in static/img/blocks/programs/,
 * and reference it here. Dark workspace backgrounds are shown on a white card.
 *
 *   <BlockShot src="/img/blocks/programs/square-function.png"
 *     alt="square(side_length) function and a call with side_length 35"
 *     caption="The square function, and calling it with side_length 35." />
 */
export function BlockShot({src, alt = 'XRP Code block program', caption, maxWidth = 480}) {
  const url = useBaseUrl(src);
  return (
    <figure className="blockProgram">
      <div className="blockShot">
        <img src={url} alt={alt} style={{maxWidth: `min(${maxWidth}px, 100%)`}} />
      </div>
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

function BlockImg({name, alt}) {
  const src = useBaseUrl(`/img/blocks/${name}.png`);
  return <img className="blockProgram__block" src={src} alt={alt || `${name} block`} />;
}

function BlockNode({item}) {
  const node = typeof item === 'string' ? {name: item} : item;
  const hasChildren = Array.isArray(node.children) && node.children.length > 0;

  const header = (
    <div className="blockProgram__row">
      <BlockImg name={node.name} alt={node.alt} />
      {node.note && <span className="blockProgram__note">← {node.note}</span>}
    </div>
  );

  if (!hasChildren) return header;

  return (
    <div className="blockGroup">
      {header}
      <div className="blockGroup__body" style={{borderColor: containerColor(node.name)}}>
        {node.children.map((c, i) => (
          <BlockNode item={c} key={i} />
        ))}
      </div>
    </div>
  );
}

export function BlockProgram({blocks = [], caption}) {
  return (
    <figure className="blockProgram">
      <div className="blockProgram__canvas">
        {blocks.map((b, i) => (
          <BlockNode item={b} key={i} />
        ))}
      </div>
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}
