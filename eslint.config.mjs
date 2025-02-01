import globals from "globals";
import tseslint from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import pluginReact from "eslint-plugin-react";

/** @type {import('eslint').Linter.FlatConfig[]} */
export default [
  {
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"], // 対象ファイル
    languageOptions: {
      parser: tsParser, // TypeScript パーサ
      globals: globals.browser, // ブラウザ用のグローバル
    },
    plugins: {
      "@typescript-eslint": tseslint,
      react: pluginReact,
    },
    rules: {
      ...tseslint.configs.recommended.rules, // typescript-eslint の推奨ルール
      ...pluginReact.configs.recommended.rules, // react の推奨ルール
      "@typescript-eslint/no-this-alias": "off", // 'this'エイリアスの警告を無効化
      "@typescript-eslint/no-unused-vars": [
        "warn",
        { argsIgnorePattern: "^_", varsIgnorePattern: "^ignored" },
      ],
      "@typescript-eslint/no-unused-expressions": [
        "warn",
        { allowShortCircuit: true, allowTernary: true },
      ],
      "react/jsx-uses-react": "off", // JSX トランスフォーム対応
      "react/react-in-jsx-scope": "off",
    },
    settings: {
      react: {
        version: "detect", // 自動検出を有効化
      },
    },
  },
];
