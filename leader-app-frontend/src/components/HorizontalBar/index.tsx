import * as React from "react";
import styles from "./HorizontalBar.module.scss";
import { motion } from "framer-motion";
import { useAnswer } from "@/hooks/Answer.context";

interface Props {
  width: number;
  votes: number;
  index: number;
  label: string;
  roundId?: number;
}

const HorizontalBar = ({ width, votes, index, label, roundId }: Props) => {
  const { labelWidth, handleWidthChange } = useAnswer();
  const rootBackground = React.useMemo(() => {
    switch (index) {
      case 0:
        return "linear-gradient(270deg, #82AC73 27.43%, #34A853 97.7%)";
      case 1:
        return "linear-gradient(270deg, #FF6161 0%, #F23225 100%)";
      case 2:
        return "linear-gradient(270deg, #22AFFF 0%, #227AFF 100%)";
      default:
        break;
    }
  }, [index]);

  const background = React.useMemo(() => {
    switch (index) {
      case 0:
        return "linear-gradient(90deg, #82AC73 27.43%, #34A853 97.7%)";
      case 1:
        return "linear-gradient(90deg, #FF6161 0%, #F23225 100%)";
      case 2:
        return "linear-gradient(90deg, #22AFFF 0%, #227AFF 100%)";
      default:
        break;
    }
  }, [index]);

  const barColor = React.useMemo(() => {
    switch (index) {
      case 0:
        return "#1F8B3C";
      case 1:
        return "#D90F02";
      case 2:
        return "#1660CF";
      default:
        break;
    }
  }, [index]);

  const ref = React.useRef<HTMLDivElement>(null);

  React.useEffect(() => {
    if (ref.current && labelWidth) {
      if (!labelWidth) {
        ref.current.style.removeProperty("width");
      }

      if (labelWidth) {
        const dimensions = ref.current.getBoundingClientRect();
        if (dimensions.width < labelWidth) {
          ref.current.style.width = `${labelWidth}px`;
        }
      }
    }
  }, [ref, labelWidth]);

  React.useEffect(() => {
    setTimeout(() => {
      if (ref.current) {
        const dimensions = ref.current.getBoundingClientRect();
        handleWidthChange(dimensions.width);
      }
    }, 50);
  }, [ref, handleWidthChange, roundId]);

  return (
    <div className={styles.container}>
      <div
        ref={ref}
        style={{ background: rootBackground }}
        className={styles.root}
      >
        <p className={styles.answer}>{label}</p>
        <p className={styles.votes}>{votes} votes</p>
      </div>
      <motion.div
        initial={{ width: 0 }}
        animate={{ width: `${width}%` }}
        // transition={{ ease: [0.17, 0.67, 0.83, 0.67] }}
        // transition={{ type: "spring", bounce: 0.25 }}
        // transition={{ type: "inertia", velocity: 100 }}
        // transition={{
        //   duration: 0.05,
        //   type: "spring",
        //   damping: 3,
        //   stiffness: 150,
        //   restDelta: 0.001,
        // }}
        style={{ background }}
      ></motion.div>
      <div
        className={styles.bar}
        style={{
          background: barColor,
        }}
      />
    </div>
  );
};

export default HorizontalBar;
