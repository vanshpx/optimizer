import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Formats a long comma-separated location string into a cleaner version.
 * Keeps the first segment (POI) and the last two segments (City, Country).
 * Example: "Airport (POI), Amausi, Lucknow (City), Uttar Pradesh, India (Country)" 
 * -> "Airport (POI), Lucknow (City), India (Country)"
 */
export function formatLocation(location: string | null | undefined): string {
  if (!location) return "";
  const segments = location.split(",").map(s => s.trim());

  if (segments.length <= 3) {
    return location;
  }

  // Keep first segment (index 0) and last two segments (length-2, length-1)
  // Per user's example "Airport (0), Lucknow (-3), India (-1)"
  // The user said "first segment" and "last two comma-separated segments".
  // In the example: POI (0), Lucknow (-3), India (-1). Lucknow is -3, India is -1.
  // Wait, let's re-read the example:
  // Input: "Chaudhary Charan Singh International Airport (LKO), Amausi, Lucknow, Uttar Pradesh, India"
  // Output: "Chaudhary Charan Singh International Airport (LKO), Lucknow, India"
  // Segments: 
  // [0] Chaudhary Charan Singh International Airport (LKO)
  // [1] Amausi
  // [2] Lucknow
  // [3] Uttar Pradesh
  // [4] India
  // Length is 5.
  // Output keeps [0], [2], [4].
  // [0] is first. [2] is Lucknow (city). [4] is India (country).
  // In many Google addresses: POI, Area, City, State, Country.
  // Lucknow is indeed the city (index length - 3).
  // India is the country (index length - 1).
  // So: segments[0], segments[segments.length - 3], segments[segments.length - 1].

  const first = segments[0];
  const city = segments[segments.length - 3];
  const country = segments[segments.length - 1];

  return `${first}, ${city}, ${country}`;
}

