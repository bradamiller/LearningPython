import React, {useState} from 'react';

/**
 * Interactive knowledge check — single-answer multiple choice with instant
 * feedback. Works for true/false and matching-style questions too (just make
 * the options the choices).
 *
 * Usage in MDX:
 *   <KnowledgeCheck
 *     question="Why does the XRP have two motors instead of one?"
 *     options={[
 *       {text: 'So it can carry more weight'},
 *       {text: 'So each wheel can turn at a different speed, letting the robot steer', correct: true},
 *       {text: 'As a backup in case one breaks'},
 *     ]}
 *     explanation="Independent wheel speeds are how a differential-drive robot turns."
 *   />
 */
export default function KnowledgeCheck({question, options = [], explanation}) {
  const [picked, setPicked] = useState(null);
  const answered = picked !== null;
  const correctIndex = options.findIndex((o) => o.correct);
  const isCorrect = answered && options[picked]?.correct;

  return (
    <div className="knowledgeCheck">
      <div className="knowledgeCheck__head">
        <span className="knowledgeCheck__badge">Knowledge Check</span>
      </div>
      <p className="knowledgeCheck__q">{question}</p>

      {options.map((opt, i) => {
        let cls = 'kcOption';
        let mark = '';
        if (answered) {
          if (i === correctIndex) {
            cls += ' kcOption--correct';
            mark = '✓';
          } else if (i === picked) {
            cls += ' kcOption--wrong';
            mark = '✕';
          }
        }
        return (
          <button
            key={i}
            type="button"
            className={cls}
            disabled={answered}
            onClick={() => setPicked(i)}>
            {opt.text}
            {mark && <span className="kcOption__mark">{mark}</span>}
          </button>
        );
      })}

      {answered && (
        <div className={`kcFeedback ${isCorrect ? 'kcFeedback--correct' : 'kcFeedback--wrong'}`}>
          <strong>{isCorrect ? 'Correct! ' : 'Not quite. '}</strong>
          {isCorrect
            ? explanation || 'Nice work.'
            : (options[correctIndex]?.feedback ||
               explanation ||
               'Review the section above and try the idea again.')}
        </div>
      )}

      {answered && (
        <button type="button" className="kcReset" onClick={() => setPicked(null)}>
          ↻ Try again
        </button>
      )}
    </div>
  );
}
