import React from "react";
import { useQuery } from "@apollo/client";
import PostItem from "../post-item";
import { GET_POSTS } from "../../queries/getPosts";

const PostList = () => {
  const { loading, data, error } = useQuery(GET_POSTS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: { error.message }</p>

  return (
    <>
      <h2>Recent Posts</h2>
      {data && data.allPosts.map(post => (
        <PostItem key={post.slug} post={post} />
      ))}
    </>
  );
};

export default PostList;
