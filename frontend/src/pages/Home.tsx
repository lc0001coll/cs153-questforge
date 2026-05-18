import { useEffect, useState } from "react";
import { fetchJson } from "../api/client";

type HealthResponse = {
  status: "ok";
  db: "ok" | "error";
};

type BackendStatus = "loading" | "ok" | "unreachable";

export default function Home() {
  const [status, setStatus] = useState<BackendStatus>("loading");
  const [dbStatus, setDbStatus] = useState<string>("");

  useEffect(() => {
    let cancelled = false;
    fetchJson<HealthResponse>("/api/health")
      .then((data) => {
        if (cancelled) return;
        setStatus("ok");
        setDbStatus(data.db);
      })
      .catch(() => {
        if (cancelled) return;
        setStatus("unreachable");
      });
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <main className="home">
      <h1>Questforge</h1>
      <p className="tagline">Multiplayer AI Dungeon Master — scaffolding</p>
      <p>
        Backend: <strong>{status === "loading" ? "checking..." : status}</strong>
      </p>
      {status === "ok" && (
        <p>
          Database: <strong>{dbStatus}</strong>
        </p>
      )}
    </main>
  );
}
