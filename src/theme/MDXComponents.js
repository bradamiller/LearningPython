import MDXComponents from '@theme-original/MDXComponents';
import TeacherNote from '@site/src/components/TeacherNote';
import KnowledgeCheck from '@site/src/components/KnowledgeCheck';
import {Video, Figure} from '@site/src/components/Media';
import {Block, BlockProgram, BlockShot} from '@site/src/components/Blocks';
import {
  LessonHeader,
  Objectives,
  TeacherBanner,
  CardGrid,
  InfoCard,
} from '@site/src/components/Lesson';

// Register curriculum components globally so lesson .mdx files can use them
// as plain tags — no per-file import lines.
export default {
  ...MDXComponents,
  TeacherNote,
  KnowledgeCheck,
  Video,
  Figure,
  Block,
  BlockProgram,
  BlockShot,
  LessonHeader,
  Objectives,
  TeacherBanner,
  CardGrid,
  InfoCard,
};
