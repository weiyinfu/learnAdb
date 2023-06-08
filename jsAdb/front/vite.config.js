import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";
// https://vitejs.dev/config/
export default defineConfig({
  base: "./",
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
    // 忽略后缀名的配置选项, 添加 .vue 选项时要记得原本默认忽略的选项也要手动写入
    extensions: [".ts", ".vue", ".js"],
  },
  build: {
    rollupOptions: {
      input: {
        main: path.resolve(__dirname, "index.html"),
        nested: path.resolve(__dirname, "haha.html"),
      },
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://localhost:7788",
        ws: true,
        changeOrigin: true,
      },
    },
  },
});
