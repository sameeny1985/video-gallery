export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b bg-white">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4">
          <div className="text-xl font-bold tracking-tight">
            Video Discovery Platform
          </div>
          <nav className="flex gap-4 text-sm">
            <a href="#explore" className="hover:underline">
              Explore
            </a>
            <a href="#promote" className="hover:underline">
              Promote
            </a>
            <a
              href="http://localhost:8000/accounts/login/"
              className="rounded-md bg-indigo-600 px-3 py-1.5 text-white"
            >
              Sign in with Google
            </a>
          </nav>
        </div>
      </header>

      <section className="mx-auto max-w-6xl px-4 py-20 text-center">
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
          Discover Videos. Connect with Creators.
          <br />
          Promote Your Content.
        </h1>
        <p className="mx-auto mt-6 max-w-2xl text-lg text-slate-600">
          A professional marketplace for creators to showcase videos, reach
          relevant audiences, and grow through transparent, platform-based
          advertising.
        </p>
        <div className="mt-10 flex flex-wrap justify-center gap-4">
          <a
            href="#explore"
            className="rounded-lg bg-indigo-600 px-6 py-3 font-medium text-white shadow hover:bg-indigo-700"
          >
            Explore Videos
          </a>
          <a
            href="#promote"
            className="rounded-lg border border-slate-300 bg-white px-6 py-3 font-medium shadow-sm hover:bg-slate-50"
          >
            Promote Your Content
          </a>
        </div>
      </section>

      <section id="explore" className="border-t bg-white py-16">
        <div className="mx-auto max-w-6xl px-4">
          <h2 className="text-2xl font-semibold">Featured Videos</h2>
          <p className="mt-2 text-slate-600">
            Placeholder – will be powered by the Django API once Phase 1 is
            complete.
          </p>
          <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {[1, 2, 3].map((i) => (
              <div
                key={i}
                className="rounded-xl border bg-slate-50 p-4 shadow-sm"
              >
                <div className="aspect-video rounded-lg bg-slate-200" />
                <h3 className="mt-3 font-medium">Sample Video {i}</h3>
                <p className="text-sm text-slate-500">Creator Channel</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <footer className="border-t py-10 text-center text-sm text-slate-500">
        <p>
          © 2026 Video Discovery Platform · Independent advertising marketplace
        </p>
        <p className="mt-1">
          Not affiliated with YouTube. Platform stats only.
        </p>
      </footer>
    </main>
  );
}
