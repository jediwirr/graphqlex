import { gql } from "@apollo/client";

export const GET_POSTS = gql`
  query {
    allPosts {
      title
      subtitle
      publishDate
      published
      metaDescription
      slug
      author {
        user {
          username
          firstName
          lastName
        }
      }
      tags {
        name
      }
    }
  }
`;
