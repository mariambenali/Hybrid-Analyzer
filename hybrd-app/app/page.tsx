"use client";

import { useRouter } from "next/navigation";

export default function HomePage() {
  const router = useRouter();

  return (
    <div className="bg-[url('/images/11.jpg')] bg-cover bg-center h-screen w-screen flex items-center justify-center">

      <div className="rounded-full h-[550px] w-[550px] flex flex-col items-center justify-center text-center p-10 bg-gradient-to-br from-blue-900 to-purple-900 shadow-2xl opacity-90">

        <h1 className="text-white text-4xl font-bold mb-4">
          MARIBEN SUMMARIZER
        </h1>

        <div className="flex gap-6 mt-4">
          <button
            onClick={() => router.push("/login")}
            className="px-6 py-2 rounded-full border border-cyan-400 text-cyan-300 hover:bg-cyan-400 hover:text-black transition"
          >
            Click here to connect
          </button>

          
        </div>

        <p className="text-white mt-6 font-bold">L'outil IA qui transforme l'information en clarté.</p>
      </div>
    </div>
  );
}