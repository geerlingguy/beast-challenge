import { useAnswer } from "@/hooks/Answer.context";
import { useBaseQuery } from "@/hooks/useCustomQuery";
import * as React from "react";
import HorizontalBar from "../HorizontalBar";
import styles from "./Answer.module.scss";

interface ISingleAnswer {
  label: string;
  percentage_of_vote_so_far: number;
  percentage_of_vote_so_far_with_t: string;
  percentage_round_participants: number;
  total: number;
}

interface IRound {
  close_time: Date;
  is_accepting_votes: number;
  is_allowing_multiple_votes: number;
  live: number;
  live_colors: number;
  round_id: number;
  start_time: Date;
  total_participants: number;
  value_0: string;
  value_1: string;
  value_2: string;
}

const Answer = () => {
  const { data: items, refetch } = useBaseQuery<ISingleAnswer[]>("/live/tally");
  const { data: round, refetch: refetchRound } =
    useBaseQuery<IRound>("/live/round");

  const { resetWidth } = useAnswer();

  React.useEffect(() => {
    const interval = setInterval(() => {
      refetch();
      refetchRound();
    }, 500);

    return () => clearInterval(interval);
  }, [refetch, refetchRound]);

  React.useEffect(() => {
    resetWidth();
  }, [round, resetWidth]);

  const totalVotes = React.useMemo(() => {
    if (!items) return 0;
    return items.reduce((acc, item) => acc + item.total, 0);
  }, [items]);

  if (!items) return null;

  return (
    <div className={styles.root}>
      {items.map((item, index) => (
        <HorizontalBar
          roundId={round?.round_id}
          key={item.label}
          votes={item.total}
          label={item.label}
          index={index}
          width={(item.total / totalVotes) * 100}
        />
      ))}
    </div>
  );
};

export default Answer;
