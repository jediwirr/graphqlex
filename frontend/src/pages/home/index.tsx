import React, { FC } from "react";
import { useQuery } from "@apollo/client";
import PostList from "./components/post-list";
import { GET_POSTS } from "./queries/getPosts";

const HomePage: FC = () => {
  const { loading, data, error } = useQuery(GET_POSTS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: { error.message }</p>

  return (
    <>
      <h2>Recent Posts</h2>
      <PostList posts={data.allPosts} />
    </>
  );
}

export default HomePage;
