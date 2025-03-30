import { z } from "zod"

export const maintenanceReqValidation = z.object({
    title: z.string().min(1, { message: "Title cannot be empty" }),
    description: z.string().refine((html) => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const textContent = doc.body.textContent?.trim() ?? "";
        return textContent.length > 0;
      }, {
        message: "HTML must contain non-empty text"
    })
})

export type MaintenanceRequest = z.infer<typeof maintenanceReqValidation>;