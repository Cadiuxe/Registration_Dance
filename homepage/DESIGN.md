---
name: Kinetic Crimson
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#e3bebb'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3031'
  outline: '#aa8987'
  outline-variant: '#5b403f'
  surface-tint: '#ffb3b0'
  primary: '#ffb3b0'
  on-primary: '#68000f'
  primary-container: '#be1e2d'
  on-primary-container: '#ffd3d1'
  inverse-primary: '#b91a2a'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#606262'
  on-tertiary-container: '#dddede'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b0'
  on-primary-fixed: '#410006'
  on-primary-fixed-variant: '#930019'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  display-lg:
    fontFamily: anybody
    fontSize: 80px
    fontWeight: '800'
    lineHeight: 90px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: anybody
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
  headline-lg-mobile:
    fontFamily: anybody
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: anybody
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  container-max-width: 1280px
---

## Brand & Style

The design system is engineered for the high-stakes, high-energy world of competitive dance. It targets an audience of elite performers, choreographers, and fans who value professionalism infused with dramatic flair. The emotional response is one of urgency, passion, and prestige.

The visual style is **High-Contrast / Bold** with elements of **Glassmorphism**. It utilizes a "dark mode by default" philosophy to make the vibrant red accents and white typography pop with maximum intensity. Abstract, flowing red ribbon motifs serve as the primary organic element, contrasting against a rigid, structured grid to represent the blend of fluid movement and disciplined technique inherent in dance.

## Colors

The palette is centered on a visceral, blood-red primary color that commands attention. 

- **Primary (Vibrant Red):** Used for calls-to-action, active states, and decorative "ribbon" elements. 
- **Background (Deep Charcoal):** A near-black base that provides the necessary depth for dramatic lighting effects.
- **Surface (Dark Grey):** Used for cards and containers to create subtle separation from the background.
- **Text (White/Grey):** Pure white is reserved for primary headings and critical information to ensure high legibility. A medium grey is used for secondary body text to maintain visual hierarchy and reduce eye strain.

## Typography

This design system utilizes a powerful mix of variable-width and geometric sans-serifs. 

**Anybody** is the display choice; its wide, aggressive stance mirrors the athleticism of dance. Use it for major headlines and titles. **Montserrat** provides a clean, modern, and highly readable foundation for all body copy and descriptions. **Space Grotesk** is used for technical labels, dates, and metadata to inject a hint of "tech-pro" precision into the championship statistics.

All large headlines should be set with tight letter spacing to increase the feeling of density and power. Labels should be set in uppercase with generous tracking for a professional, "proposal-style" finish.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to maintain a premium, editorial feel, transitioning to a fluid model for mobile devices. 

- **Desktop:** 12-column grid with wide 64px margins. This creates "stage-like" focus in the center of the screen.
- **Mobile:** 4-column grid with 16px margins. 
- **Rhythm:** An 8px linear scale is used for all internal padding and component spacing. Content sections are separated by large vertical gaps (80px - 120px) to allow the "ribbon" background visuals to breathe and flow between sections without cluttering the information.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layers** and **Glows** rather than traditional drop shadows.

1. **Floor:** The `#0A0A0A` background.
2. **Plinth:** Cards and containers use `#1A1A1A` with a subtle 1px solid border in `#BE1E2D` (at 30% opacity) to define edges.
3. **Focus:** Interactive elements like active buttons use a "Crimson Glow"—a diffused outer shadow of the primary red color (`rgba(190, 30, 45, 0.4)`) with a 20px blur.
4. **Overlays:** Modals and navigation bars use a backdrop blur (20px) and a semi-transparent black fill to maintain the dark aesthetic while indicating depth.

## Shapes

The shape language is **Soft** but disciplined. Small radius corners (4px) on cards and inputs suggest precision and modern structure. 

Buttons and chips use a more aggressive **Pill-shape** (rounded-full) to provide a visual break from the rectangular grid, echoing the fluid curves of the red ribbon graphics. The contrast between sharp grid lines and pill-shaped interactive elements helps users quickly identify clickable zones.

## Components

- **Buttons:** Primary buttons feature a subtle vertical gradient from the primary red to a slightly darker shade. Hover states should increase the "Crimson Glow" elevation. Secondary buttons use a transparent background with a 2px white or red border.
- **Cards:** Dark-themed with a top-heavy layout. Use a 4px red accent bar at the top of cards to categorize different competition types (e.g., Solo vs. Group).
- **Inputs:** Dark grey backgrounds (`#1A1A1A`) with bottom-only borders that turn primary red on focus. Use Space Grotesk for placeholder text.
- **Chips/Badges:** Small, pill-shaped elements used for "Season 2" or "Register Now" tags. These should use white text on a primary red background for maximum visibility.
- **Background Visuals:** Large-scale SVG or high-resolution PNG "ribbons" should be positioned absolutely behind content, often bleeding off the edge of the screen to create a sense of continuous motion.