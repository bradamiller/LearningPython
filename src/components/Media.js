import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

/**
 * Site-root paths like /img/x.jpg must go through useBaseUrl, or they break the
 * moment the site is served from a subpath (GitHub Pages project sites are
 * served from /<repo>/). External URLs and data: URIs are passed through
 * untouched.
 */
function useMediaUrl(src) {
  const resolved = useBaseUrl(src || '');
  if (!src) return src;
  if (/^(https?:)?\/\//.test(src) || src.startsWith('data:')) return src;
  return resolved;
}

/**
 * Video block. If you pass `src` (a YouTube/Vimeo embed URL or a local
 * /videos/foo.mp4), it renders the real player. With no src it shows a
 * labeled placeholder so you can see exactly where your video will go and
 * drop it in later.
 *
 * Usage:
 *   <Video caption="XRP driving forward and back" placeholderLabel="Intro hook clip (1–2 min)" />
 *   <Video src="https://www.youtube.com/embed/XXXX" caption="Hardware tour" />
 *   <Video src="/videos/first-drive.mp4" mp4 caption="First upload" />
 */
export function Video({src, mp4 = false, caption, placeholderLabel = 'Video goes here'}) {
  const url = useMediaUrl(src);
  return (
    <figure className="videoBlock">
      {src ? (
        <div className="videoBlock__frame">
          {mp4 ? (
            <video controls src={url} />
          ) : (
            <iframe src={url} title={caption || 'video'} allowFullScreen />
          )}
        </div>
      ) : (
        <div className="videoPlaceholder">
          <div className="videoPlaceholder__play">▶</div>
          <div><strong>{placeholderLabel}</strong></div>
          <div className="videoPlaceholder__hint">Add a src to embed your video here</div>
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}

/**
 * Image figure. Pass `src` for a real image, or leave it out to show a
 * placeholder frame with a description of the graphic you'll create.
 *
 * Usage:
 *   <Figure src="/img/lesson-01/xrp-parts.png" alt="Labeled XRP" caption="The parts of the XRP" />
 *   <Figure placeholderLabel="Labeled diagram of the XRP robot" caption="Robot hardware" />
 */
export function Figure({src, alt = '', caption, placeholderLabel = 'Graphic goes here'}) {
  const url = useMediaUrl(src);
  return (
    <figure className="videoBlock">
      {src ? (
        <img
          src={url}
          alt={alt}
          style={{borderRadius: 12, display: 'block', maxWidth: '100%', maxHeight: 520, width: 'auto', margin: '0 auto'}}
        />
      ) : (
        <div className="figurePlaceholder">
          <div className="figurePlaceholder__icon">🖼️</div>
          <div><strong>{placeholderLabel}</strong></div>
          <div className="videoPlaceholder__hint">Add a src to drop in your image</div>
        </div>
      )}
      {caption && <figcaption className="mediaCaption">{caption}</figcaption>}
    </figure>
  );
}
