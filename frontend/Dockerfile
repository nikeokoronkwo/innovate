FROM node:20-slim AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
COPY . /app
WORKDIR /app

FROM base AS build
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --frozen-lockfile
RUN pnpm run build

FROM base
COPY --from=build /app/.output /app/.output

ENV NUXT_DJANGO_ACTIVE=1

EXPOSE 3000
CMD [ "node", "--env-file=.env", ".output/server/index.mjs" ]