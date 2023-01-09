import React, { FC } from "react";
import PostItem from "../post-item";

type Props = {
  posts: any[];
}

const PostList: FC<Props> = (props) => {
  const { posts } = props;

  return (
    <>
      {posts.map((post: any) => (
        <PostItem key={post.slug} post={post} />
      ))}
    </>
  );
};

export default PostList;
