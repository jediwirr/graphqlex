import React, { FC } from "react";

type Props = {
  post: any;
}

const PostItem: FC<Props> = (props) => {
  const { post } = props;
  const {
    title,
    subtitle,
    author,
    publishDate,
    metaDescription,
    body
  } = post;

  return (
    <div className="post">
      <h2>{title}: {subtitle}</h2>
      By {author.user.username}
      <p className="post__description">
        {metaDescription}
      </p>
      <article>
        {body}
      </article>
    </div>
  );
};

export default PostItem;
