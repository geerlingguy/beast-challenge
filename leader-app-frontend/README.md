# Leader App Frontend

Next.js Frontend Application to view vote results

## Local Development

NPM is used to manage packages. To install packages run `npm install`

Create a new `.env.local` file using `.env.example`. Following are the env variable used.

```
NEXT_PUBLIC_BASE_URL // Endpoint of the backend flask App
```

To run development server `npm run dev`

## Production Build

1. npm run build
2. npm run start

## Libraries used

1. Framer motion -> For animation
2. react-query -> for data fetching
3. sass -> for styling
