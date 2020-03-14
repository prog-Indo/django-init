DJANGO GRAPH KEREN

https://apirobot.me/posts/django-react-ts-how-to-create-and-consume-graphql-api
https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/
https://www.howtographql.com/graphql-python/4-authentication/


DJANGO GRAPH SUBSCRIPTION
https://github.com/eamigo86/graphene-django-subscriptions

{
  notes (search:"test") {
    edges {
      node {
        title
        body
        createdAt
      }
    }
  }
}


{
  note(id: "1") {
    title
  }
}

mutation {
  noteCreate (input: {
    title: "TITLE",
    body: "BODY"
  }) {
    note {
      title,
      body,
      createdAt
    }
  }
}

DJANGO AUTHENTICATION
https://www.howtographql.com/graphql-python/4-authentication/